use std::{fmt, iter, ops::Range, sync::Arc};

use crate::{
    utils::{fmt_sep, TagDisplay},
    GraphError, GraphErrorKind,
};

pub type Tag = Arc<str>;

#[derive(Debug, Clone)]
pub enum Expr {
    Tag(Tag, Range<usize>),
    Group(Vec<Expr>, bool),
    Neg(Box<Expr>),
}
impl Default for Expr {
    fn default() -> Self {
        Self::Group(vec![], true)
    }
}
impl Expr {
    pub fn span(&self) -> Range<usize> {
        match self {
            Self::Tag(_, span) => span.clone(),
            Self::Group(nodes, _) => {
                if nodes.is_empty() {
                    return 0..0;
                }
                let first = nodes[0].span();
                let last = nodes[nodes.len() - 1].span();
                first.start..last.end
            }
            Self::Neg(node) => {
                let span = node.span();
                (span.start - 1)..span.end
            }
        }
    }

    pub fn concat(nodes: impl IntoIterator<Item = Expr>, ands: bool) -> Self {
        let mut result = vec![];
        for node in nodes {
            match node {
                Expr::Group(nodes, its_ands) if its_ands == ands => {
                    result.extend(nodes);
                }
                _ => result.push(node),
            }
        }
        if result.len() == 1 {
            result.remove(0)
        } else {
            Self::Group(result, ands)
        }
    }

    pub fn is_any(&self) -> bool {
        matches!(self, Self::Group(nodes, true) if nodes.is_empty())
    }

    pub fn to_tags<'a>(&'a self) -> Box<dyn Iterator<Item = Result<Tag, GraphError>> + 'a> {
        let span = self.span();
        match self {
            Expr::Tag(tag, _) => Box::new(iter::once(Ok(tag.clone()))),
            Expr::Group(nodes, true) => Box::new(nodes.iter().map(move |it| match it {
                Expr::Tag(tag, _) => Ok(tag.clone()),
                _ => Err(GraphErrorKind::InvalidTags.with_span(span.clone())),
            })),
            _ => Box::new(iter::once(Err(
                GraphErrorKind::InvalidTags.with_span(span.clone())
            ))),
        }
    }
}

impl fmt::Display for Expr {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Self::Tag(tag, _) => TagDisplay(tag.as_ref()).fmt(f),
            Self::Group(nodes, ands) => {
                write!(f, "(")?;
                fmt_sep(f, nodes.iter(), if *ands { ", " } else { " / " })?;
                write!(f, ")")
            }
            Self::Neg(node) => write!(f, "-{node}"),
        }
    }
}
