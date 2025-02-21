use logos::{Lexer, Logos};
use std::{fmt, mem, ops::Range};

use crate::{GraphError, Implication, Query, RawGraph, RawSubject, TagGraph};

mod parsers;

#[derive(Logos, Debug, Clone, Copy, PartialEq, Eq)]
#[logos(skip r"[ \t]+")] // Ignore this regex pattern between tokens
pub enum Token {
    #[token(":")]
    Colon,

    #[token(".")]
    Period,

    #[token("->")]
    Arrow,

    #[token("=")]
    Eq,

    #[token("/")]
    Or,

    #[token(",")]
    Comma,

    #[token("(")]
    LParen,

    #[token(")")]
    RParen,

    #[token("[")]
    LBracket,

    #[token("]")]
    RBracket,

    #[token("{")]
    LBrace,

    #[token("}")]
    RBrace,

    #[token("-")]
    Neg,

    #[token("\n")]
    Newline,

    #[regex(r#""([^"\\]|\\["\\bnfrt]|u[a-fA-F0-9]{4})*""#)]
    #[regex(r"[\w·'_][\w·'_\-]*([ ]+([\w·'_][\w·'_\-]*)?)*")]
    Tag,
}

#[derive(Debug)]
enum GotToken {
    Eof,
    Token(Token),
    Unrecognized,
}

#[derive(Debug)]
pub struct SyntaxError {
    got: GotToken,
    position: usize,
    context: Option<&'static str>,
    expecting: Option<&'static str>,
}
impl SyntaxError {
    fn new(got: GotToken, context: Option<&'static str>, position: usize) -> Self {
        Self {
            got,
            position,
            context,
            expecting: None,
        }
    }

    pub fn position(&self) -> usize {
        self.position
    }

    pub fn expecting(mut self, expecting: &'static str) -> Self {
        self.expecting = Some(expecting);
        self
    }
}

impl fmt::Display for SyntaxError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "at position {}: ", self.position)?;
        if let Some(ctx) = &self.context {
            write!(f, "invalid {ctx}: ")?;
        }
        match &self.got {
            GotToken::Eof => write!(f, "unexpected eof"),
            GotToken::Token(token) => write!(f, "unexpected {token:?}"),
            GotToken::Unrecognized => write!(f, "unrecognized token"),
        }?;
        if let Some(expecting) = &self.expecting {
            write!(f, ", expecting {expecting}")?;
        }
        Ok(())
    }
}

pub type ParseResult<T = ()> = Result<T, SyntaxError>;

trait ParserFn<T>: Sized {
    fn parse(&mut self, parser: &mut Parser) -> ParseResult<T>;

    fn spanned(mut self) -> impl ParserFn<(T, Range<usize>)> {
        move |parser: &mut Parser| {
            let mut start = parser.position();
            let rem = &parser.lexer.source()[start..];
            start += rem.len() - rem.trim_start().len();
            let result = self.parse(parser)?;
            Ok((result, start..parser.position()))
        }
    }
}

impl<F, T> ParserFn<T> for F
where
    F: FnMut(&mut Parser) -> ParseResult<T>,
{
    fn parse(&mut self, parser: &mut Parser) -> ParseResult<T> {
        self(parser)
    }
}
impl ParserFn<()> for Token {
    fn parse(&mut self, parser: &mut Parser) -> ParseResult<()> {
        parser.expect(*self)
    }
}

fn sep1<T>(mut f: impl ParserFn<T>, sep: Token) -> impl ParserFn<Vec<T>> {
    move |p: &mut Parser| {
        let mut result = vec![f.parse(p)?];
        while p.try_expect(sep)? {
            result.push(f.parse(p)?);
        }
        Ok(result)
    }
}
fn comma1<T>(f: impl ParserFn<T>) -> impl ParserFn<Vec<T>> {
    sep1(f, Token::Comma)
}

fn preceded<R, T>(mut ignored: impl ParserFn<R>, mut f: impl ParserFn<T>) -> impl ParserFn<T> {
    move |p: &mut Parser| {
        ignored.parse(p)?;
        f.parse(p)
    }
}
fn terminated<R, T>(mut f: impl ParserFn<T>, mut ignored: impl ParserFn<R>) -> impl ParserFn<T> {
    move |p: &mut Parser| {
        let result = f.parse(p)?;
        ignored.parse(p)?;
        Ok(result)
    }
}

fn delimited<R1, R2, T>(
    left: impl ParserFn<R1>,
    right: impl ParserFn<R2>,
    f: impl ParserFn<T>,
) -> impl ParserFn<T> {
    preceded(left, terminated(f, right))
}

fn eof_ok<T>(result: ParseResult<T>) -> ParseResult<Option<T>> {
    match result {
        Err(SyntaxError {
            got: GotToken::Eof, ..
        }) => Ok(None),
        Err(err) => Err(err),
        Ok(value) => Ok(Some(value)),
    }
}

struct Parser<'s> {
    lexer: Lexer<'s, Token>,
    look_ahead: Option<Token>,
    context: Option<&'static str>,
}

impl<'s> Parser<'s> {
    pub fn new(lexer: Lexer<'s, Token>) -> Self {
        Self {
            lexer,
            look_ahead: None,
            context: None,
        }
    }

    fn next(&mut self) -> ParseResult<Token> {
        if let Some(token) = self.look_ahead.take() {
            return Ok(token);
        }
        match self.lexer.next() {
            None => Err(SyntaxError::new(
                GotToken::Eof,
                self.context,
                self.lexer.source().len(),
            )),
            Some(Ok(token)) => Ok(token),
            Some(Err(_)) => Err(SyntaxError::new(
                GotToken::Unrecognized,
                self.context,
                self.lexer.span().end,
            )),
        }
    }
    fn peek(&mut self) -> ParseResult<Token> {
        if self.look_ahead.is_none() {
            self.look_ahead = Some(self.next()?);
        }
        Ok(self.look_ahead.unwrap())
    }

    fn expect(&mut self, expected: Token) -> ParseResult<()> {
        let token = self.peek()?;
        if token == expected {
            self.next()?;
            Ok(())
        } else {
            Err(self.unexpected(token))
        }
    }
    fn try_expect(&mut self, expected: Token) -> ParseResult<bool> {
        let token = eof_ok(self.peek())?;
        if token == Some(expected) {
            self.next()?;
            Ok(true)
        } else {
            Ok(false)
        }
    }

    fn unexpected(&self, token: Token) -> SyntaxError {
        SyntaxError::new(GotToken::Token(token), self.context, self.position())
    }

    fn unrecognized(&self) -> SyntaxError {
        SyntaxError::new(GotToken::Unrecognized, self.context, self.position())
    }

    fn position(&self) -> usize {
        let span = self.lexer.span();
        if self.look_ahead.is_some() {
            span.start
        } else {
            span.end
        }
    }

    fn with_context<R>(&mut self, context: &'static str, f: impl FnOnce(&mut Self) -> R) -> R {
        let old_context = mem::replace(&mut self.context, Some(context));
        let result = f(self);
        self.context = old_context;
        result
    }
}

pub fn parse_raw(query: &str) -> Result<RawGraph, GraphError> {
    let mut parser = Parser::new(Token::lexer(query));
    parsers::raw_graph
        .parse(&mut parser)
        .map_err(GraphError::syntax_error)
}

pub fn parse_query(query: &str, inline: bool) -> Result<Query, GraphError> {
    let RawGraph {
        subject,
        meta_queries,
    } = if inline {
        let mut parser = Parser::new(Token::lexer(query));
        parsers::inline_query
            .parse(&mut parser)
            .map_err(GraphError::syntax_error)?
    } else {
        parse_raw(query)?
    };
    Query::new(subject, meta_queries, inline)
}

pub fn parse_tag_graph(graph: &str) -> Result<TagGraph, GraphError> {
    let graph = parse_raw(graph)?.subject;
    TagGraph::new(graph)
}

pub fn parse_implication(implication: &str) -> Result<Implication, GraphError> {
    let mut parser = Parser::new(Token::lexer(implication));
    parsers::implication
        .parse(&mut parser)
        .map_err(GraphError::syntax_error)
}
