use serde::{Deserialize, Serialize};
use std::{
    collections::HashMap,
    fmt, mem,
    ops::{Index, IndexMut, Range},
};

use crate::{
    parse::SyntaxError,
    utils::{fmt_sep, TagDisplay},
    Expr, MetaQuery, Tag,
};

#[derive(Debug)]
pub struct GraphError {
    pub kind: GraphErrorKind,
    pub span: Range<usize>,
}
impl fmt::Display for GraphError {
    fn fmt(&self, f: &mut fmt::Formatter) -> std::fmt::Result {
        write!(f, "({}, {}): {}", self.span.start, self.span.end, self.kind)
    }
}
impl std::error::Error for GraphError {}
impl GraphError {
    pub fn syntax_error(e: SyntaxError) -> Self {
        let span = e.position().saturating_sub(1)..e.position();
        Self {
            kind: GraphErrorKind::SyntaxError(e),
            span,
        }
    }
}

#[derive(Debug)]
pub enum GraphErrorKind {
    SyntaxError(SyntaxError),

    SubjectNotFound(String),

    DuplicateIdentities,
    DuplicateTags,
    DuplicateRelations,

    InvalidTags,
    InvalidMetaQuery(String),
}
impl fmt::Display for GraphErrorKind {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            GraphErrorKind::SyntaxError(e) => write!(f, "invalid syntax\n{e}"),
            GraphErrorKind::SubjectNotFound(subject) => write!(f, "subject not found: {subject}"),
            GraphErrorKind::DuplicateIdentities => write!(f, "duplicate identities"),
            GraphErrorKind::DuplicateTags => write!(f, "duplicate tags"),
            GraphErrorKind::DuplicateRelations => write!(f, "duplicate relations"),
            GraphErrorKind::InvalidTags => write!(f, "invalid tags"),
            GraphErrorKind::InvalidMetaQuery(msg) => write!(f, "invalid meta query: {msg}"),
        }
    }
}
impl GraphErrorKind {
    pub fn with_span(self, span: Range<usize>) -> GraphError {
        GraphError { kind: self, span }
    }
}

#[derive(
    Debug, Default, Clone, Copy, Hash, PartialEq, Eq, PartialOrd, Ord, Serialize, Deserialize,
)]
#[repr(transparent)]
#[serde(transparent)]
pub struct SubjectId(pub usize);

#[derive(Serialize, Deserialize)]
#[serde(transparent)]
pub struct SubjectIndexed<T>(pub Vec<T>);
impl<T> Index<SubjectId> for SubjectIndexed<T> {
    type Output = T;

    fn index(&self, index: SubjectId) -> &Self::Output {
        &self.0[index.0]
    }
}
impl<T> IndexMut<SubjectId> for SubjectIndexed<T> {
    fn index_mut(&mut self, index: SubjectId) -> &mut Self::Output {
        &mut self.0[index.0]
    }
}

pub type Subjects = SubjectIndexed<Subject>;

fn unknown_subject(subject: &SubjectRef) -> GraphError {
    GraphErrorKind::SubjectNotFound(subject.path.join(".")).with_span(subject.span.clone())
}

struct ResolveContext<'a> {
    subjects: &'a Subjects,
    relation_refs: &'a [Option<RelationRef>],
    parent: SubjectId,
    ref_map: HashMap<&'a str, SubjectId>,
}
impl ResolveContext<'_> {
    fn resolve_subject(&self, subject: &SubjectRef) -> Result<SubjectId, GraphError> {
        let mut it = subject.path.iter();
        let Some(mut n) = self.ref_map.get(it.next().unwrap().as_ref()).copied() else {
            return Err(unknown_subject(subject));
        };
        for i in it {
            match self.subjects[n]
                .children
                .iter()
                .rev()
                .find(|c| self.subjects[**c].name == Some(i.clone()))
            {
                Some(id) => n = *id,
                None => return Err(unknown_subject(subject)),
            };
        }

        Ok(n)
    }
}
struct ResolveResult<'a> {
    relations: &'a mut [Option<Relation>],
}

#[derive(Debug, Clone, Hash, PartialEq, Eq)]
pub struct Relation {
    pub source: SubjectId,
    pub target: SubjectId,
}

pub enum RelationContext {
    Explicit(SubjectId),
    Implicit(SubjectId),
}
impl RelationContext {
    pub fn get(&self) -> SubjectId {
        match self {
            RelationContext::Explicit(id) => *id,
            RelationContext::Implicit(id) => *id,
        }
    }
}

#[derive(Debug, Clone)]
pub struct RawSubject {
    pub name: Option<Tag>,
    pub identity: Option<Tag>,
    pub relation: Option<RelationRef>,
    pub expr: Expr,
    pub children: Vec<RawSubject>,
    pub span: Range<usize>,
    pub blank_line_after: bool,
}
impl RawSubject {
    fn flatten_into(
        mut self,
        subjects: &mut Subjects,
        relations: &mut Vec<Option<RelationRef>>,
        parent: Option<SubjectId>,
    ) -> Result<SubjectId, GraphError> {
        let children = mem::take(&mut self.children);
        let id = SubjectId(subjects.0.len());

        let subject = Subject {
            id,
            parent: parent.unwrap_or_default(),
            name: self.name.or_else(|| self.identity.clone()),
            identity: self.identity,
            relation: None,
            expr: self.expr,
            children: vec![],
            span: self.span,
        };
        subjects.0.push(subject);
        relations.push(self.relation);
        subjects[id].children = children
            .into_iter()
            .map(|it| it.flatten_into(subjects, relations, Some(id)))
            .collect::<Result<Vec<_>, _>>()?;

        Ok(id)
    }
}

struct IndentedRawSubject<'a> {
    inner: &'a RawSubject,
    indent: &'a str,
}
impl fmt::Display for IndentedRawSubject<'_> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        if !self.indent.is_empty() {
            write!(f, "{}", self.indent)?;
            if let Some(name) = &self.inner.name {
                if self.inner.identity.as_ref() != Some(name) {
                    write!(f, "({}) ", TagDisplay(name))?;
                }
            }
            if let Some(identity) = &self.inner.identity {
                write!(f, "{}", TagDisplay(identity))?;
            } else if let Some(rel) = &self.inner.relation {
                write!(f, "{} -> {}", rel.source, rel.target)?;
            }
            if !self.inner.expr.is_any() {
                write!(f, ": {}", UnwrapGroup(&self.inner.expr))?;
            }
            if !self.inner.children.is_empty() {
                write!(f, " ")?;
            }
        } else if !self.inner.expr.is_any() {
            writeln!(f, "{}", UnwrapGroup(&self.inner.expr))?;
        }

        if !self.inner.children.is_empty() {
            writeln!(f, "{{")?;
            let new_indent = self.indent.to_owned() + "  ";
            let mut last_has_blank_line = false;
            for child in &self.inner.children {
                if last_has_blank_line {
                    writeln!(f)?;
                }
                writeln!(
                    f,
                    "{}",
                    IndentedRawSubject {
                        inner: child,
                        indent: &new_indent
                    }
                )?;
                last_has_blank_line = child.blank_line_after;
            }
            write!(f, "{}}}", self.indent)?;
        }
        Ok(())
    }
}

struct UnwrapGroup<'a>(&'a Expr);
impl fmt::Display for UnwrapGroup<'_> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self.0 {
            Expr::Group(nodes, ands) => fmt_sep(f, nodes.iter(), if *ands { ", " } else { " / " }),
            other => write!(f, "{other}"),
        }
    }
}

impl fmt::Display for RawSubject {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        IndentedRawSubject {
            inner: self,
            indent: "",
        }
        .fmt(f)
    }
}

pub struct RawGraph {
    pub subject: RawSubject,
    pub meta_queries: Vec<MetaQuery>,
}

impl fmt::Display for RawGraph {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.subject)?;
        for query in &self.meta_queries {
            write!(f, "\n{query}")?;
        }
        Ok(())
    }
}

#[derive(Debug)]
pub struct Subject {
    pub id: SubjectId,
    pub parent: SubjectId,
    pub name: Option<Tag>,
    pub identity: Option<Tag>,
    pub relation: Option<Relation>,
    pub expr: Expr,
    pub children: Vec<SubjectId>,
    pub span: Range<usize>,
}
impl Subject {
    fn resolve(&self, cx: &ResolveContext, result: &mut ResolveResult) -> Result<(), GraphError> {
        if let Some(rel) = &cx.relation_refs[self.id.0] {
            let source = cx.parent;
            let target = cx.resolve_subject(&rel.target)?;

            result.relations[self.id.0] = Some(Relation { source, target });
        }

        if self.children.is_empty() {
            return Ok(());
        }

        let mut cx = ResolveContext {
            subjects: cx.subjects,
            relation_refs: cx.relation_refs,
            parent: self.id,
            ref_map: cx.ref_map.clone(),
        };
        for &child in &self.children {
            if let Some(name) = &cx.subjects[child].name {
                cx.ref_map.insert(name, child);
            }
        }
        for &child in &self.children {
            cx.subjects[child].resolve(&cx, result)?;
        }

        Ok(())
    }
}

#[derive(Debug, Clone)]
pub struct RelationRef {
    pub source: SubjectRef,
    pub target: SubjectRef,
}

#[derive(Debug, Clone, Serialize)]
pub struct SubjectRef {
    pub path: Vec<Tag>,
    #[serde(skip)]
    pub span: Range<usize>,
}
impl fmt::Display for SubjectRef {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt_sep(f, self.path.iter().map(|it| TagDisplay(it)), ".")
    }
}

pub struct Graph {
    pub subjects: Subjects,
}
impl Graph {
    pub(crate) fn from_raw(subject: RawSubject) -> Result<Self, GraphError> {
        let mut subjects = SubjectIndexed(vec![]);
        let mut relation_refs = vec![];
        subject.flatten_into(&mut subjects, &mut relation_refs, None)?;

        let mut relation_tuples = vec![None; subjects.0.len()];
        subjects[SubjectId(0)].resolve(
            &ResolveContext {
                subjects: &subjects,
                relation_refs: &relation_refs,
                parent: SubjectId(0),
                ref_map: HashMap::new(),
            },
            &mut ResolveResult {
                relations: &mut relation_tuples,
            },
        )?;

        for (subject, rel) in subjects.0.iter_mut().zip(relation_tuples) {
            subject.relation = rel;
        }

        Ok(Self { subjects })
    }

    pub fn resolve(&self, subject: &SubjectRef) -> Result<SubjectId, GraphError> {
        let mut result = SubjectId(0);
        for i in &subject.path {
            match self.subjects[result]
                .children
                .iter()
                .rev()
                .find(|c| self.subjects[**c].name == Some(i.clone()))
            {
                Some(id) => result = *id,
                None => return Err(unknown_subject(subject)),
            };
        }
        Ok(result)
    }

    pub fn root(&self) -> &Subject {
        &self.subjects[SubjectId(0)]
    }

    pub fn len(&self) -> usize {
        self.subjects.0.len()
    }

    pub fn is_empty(&self) -> bool {
        self.subjects.0.is_empty()
    }
}
