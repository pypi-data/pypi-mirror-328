use std::ops::Range;

use crate::{Expr, Implication, MetaQuery, RawGraph, RelationRef, SubjectRef, Tag};

use super::{
    comma1, delimited, eof_ok, preceded, sep1, terminated, ParseResult, Parser, ParserFn,
    RawSubject, Token,
};

fn eval_string_content(p: &mut Parser, s: &str) -> ParseResult<String> {
    let mut result = String::new();
    let mut chars = s.chars();
    while let Some(c) = chars.next() {
        if c == '\\' {
            let Some(c) = chars.next() else {
                unreachable!()
            };
            result.push(match c {
                'u' => {
                    let (hex, rest) = chars.as_str().split_at(4);
                    chars = rest.chars();
                    let code = u32::from_str_radix(hex, 16).unwrap();
                    match std::char::from_u32(code) {
                        Some(c) => c,
                        None => {
                            return Err(p.with_context("unicode escape", |p| p.unrecognized()));
                        }
                    }
                }
                '\\' | '"' => c,
                'b' => '\x08',
                'f' => '\x0C',
                'n' => '\n',
                'r' => '\r',
                't' => '\t',
                _ => c,
            });
        } else {
            result.push(c);
        }
    }
    Ok(result)
}

fn newline0(p: &mut Parser) -> ParseResult<u32> {
    let mut count = 0;
    while let Some(Token::Newline) = eof_ok(p.peek())? {
        p.next()?;
        count += 1;
    }
    Ok(count)
}

fn tag(p: &mut Parser) -> ParseResult<Tag> {
    p.expect(Token::Tag)?;

    let tag = p.lexer.slice().trim_end();
    Ok(match tag.as_bytes()[0] {
        b'"' => eval_string_content(p, &tag[1..tag.len() - 1])?.into(),
        _ => tag.into(),
    })
}

fn meta_query(p: &mut Parser) -> ParseResult<MetaQuery> {
    fn inner(p: &mut Parser) -> ParseResult<MetaQuery> {
        let start = p.position();
        p.with_context("meta query", |p| {
            let neg = p.try_expect(Token::Neg)?;
            let kind = tag.parse(p)?;
            p.expect(Token::Colon)?;
            let args = sep1(subject_ref, Token::Comma).parse(p)?;
            Ok(MetaQuery {
                neg,
                kind,
                args,
                span: start..p.position(),
            })
        })
    }
    delimited(Token::LBracket, Token::RBracket, inner).parse(p)
}

fn subject_ref(p: &mut Parser) -> ParseResult<SubjectRef> {
    let (path, span) = sep1(tag, Token::Period).spanned().parse(p)?;
    Ok(SubjectRef { path, span })
}

fn subject(p: &mut Parser) -> ParseResult<RawSubject> {
    p.with_context("subject", |p| {
        let begin = p.position();
        let name = if p.try_expect(Token::LParen)? {
            Some(terminated(tag, Token::RParen).parse(p)?)
        } else {
            None
        };

        let mut relation = None;
        let mut identity = None;

        if p.peek()? == Token::Tag {
            let the_ref = subject_ref.parse(p)?;
            match p.peek()? {
                Token::Arrow => {
                    // relation
                    let source = the_ref;
                    p.expect(Token::Arrow)?;
                    let target = subject_ref.parse(p)?;
                    relation = Some(RelationRef { source, target });
                }
                Token::Colon | Token::LBrace | Token::Newline | Token::RBrace => {
                    // name
                    if the_ref.path.len() > 1 {
                        return Err(p.unexpected(Token::Period).expecting("name"));
                    }
                    identity = Some(the_ref.path.into_iter().next().unwrap());
                }
                other => {
                    return Err(p.unexpected(other).expecting("relation or name"));
                }
            }
        }
        let span = begin..p.position();

        let expr = if p.try_expect(Token::Colon)? {
            expr.parse(p)?
        } else {
            Expr::default()
        };

        let children = if p.peek()? == Token::LBrace {
            subject_body.parse(p)?
        } else {
            Vec::new()
        };

        Ok(RawSubject {
            name,
            identity,
            relation,
            expr,
            children,
            span,
            blank_line_after: false,
        })
    })
}

fn subject_body(p: &mut Parser) -> ParseResult<Vec<RawSubject>> {
    p.expect(Token::LBrace)?;
    let mut result: Vec<RawSubject> = vec![];
    loop {
        let count = newline0.parse(p)?;
        if count >= 2 {
            if let Some(subject) = result.last_mut() {
                subject.blank_line_after = true;
            }
        }
        if p.try_expect(Token::RBrace)? {
            break;
        }
        result.push(subject.parse(p)?);
    }
    Ok(result)
}

fn atom(p: &mut Parser) -> ParseResult<Expr> {
    p.with_context("atom", |p| match p.peek()? {
        Token::LParen => {
            p.next()?;
            Ok(if p.try_expect(Token::RParen)? {
                Expr::default()
            } else {
                let expr = expr.parse(p)?;
                p.expect(Token::RParen)?;
                expr
            })
        }
        Token::Tag => tag
            .spanned()
            .parse(p)
            .map(|(tag, span)| Expr::Tag(tag, span)),
        Token::Neg => preceded(Token::Neg, atom)
            .parse(p)
            .map(|it| Expr::Neg(Box::new(it))),
        token => Err(p.unexpected(token)),
    })
}

fn or_term(p: &mut Parser) -> ParseResult<Expr> {
    Ok(Expr::concat(sep1(atom, Token::Or).parse(p)?, false))
}

fn expr(p: &mut Parser) -> ParseResult<Expr> {
    Ok(Expr::concat(sep1(or_term, Token::Comma).parse(p)?, true))
}

fn new_raw_graph(
    exprs: Vec<Expr>,
    children: Vec<RawSubject>,
    meta_queries: Vec<MetaQuery>,
    span: Range<usize>,
) -> RawGraph {
    RawGraph {
        subject: RawSubject {
            name: None,
            identity: None,
            relation: None,
            expr: Expr::concat(exprs, true),
            children,
            span,
            blank_line_after: false,
        },
        meta_queries,
    }
}

pub fn raw_graph(p: &mut Parser) -> ParseResult<RawGraph> {
    let start = p.position();

    let mut exprs = vec![];
    let mut children = vec![];
    let mut meta_queries = vec![];
    loop {
        newline0.parse(p)?;
        let Some(token) = eof_ok(p.peek())? else {
            break;
        };
        match token {
            Token::LBrace => {
                children.extend(subject_body.parse(p)?);
            }
            Token::LBracket => {
                meta_queries.push(meta_query.parse(p)?);
            }
            Token::Neg | Token::Tag | Token::LParen => {
                exprs.push(expr.parse(p)?);
            }
            token => {
                return Err(p
                    .unexpected(token)
                    .expecting("expression, subject or meta queries"))
            }
        }
    }

    Ok(new_raw_graph(
        exprs,
        children,
        meta_queries,
        start..p.position(),
    ))
}

pub fn inline_query(p: &mut Parser) -> ParseResult<RawGraph> {
    let start = p.position();

    let mut children = vec![];
    let mut meta_queries = vec![];
    loop {
        newline0.parse(p)?;
        let Some(token) = eof_ok(p.peek())? else {
            break;
        };
        match token {
            Token::LBracket => {
                meta_queries.push(meta_query.parse(p)?);
            }
            _ => {
                children.push(subject.parse(p)?);
            }
        }
    }

    Ok(new_raw_graph(
        vec![],
        children,
        meta_queries,
        start..p.position(),
    ))
}

pub fn implication(p: &mut Parser) -> ParseResult<Implication> {
    let condition = comma1(tag).parse(p)?;
    p.expect(Token::Arrow)?;
    let consequence = comma1(tag).parse(p)?;
    Ok(Implication {
        condition,
        consequence,
    })
}
