use std::{
    collections::{HashMap, HashSet},
    mem,
    ops::Range,
};

use crate::{Expr, Graph, GraphError, RawSubject, SubjectId, SubjectIndexed, Subjects, Tag};

pub(crate) struct IndexedExtra {
    pub tags: im::HashSet<Tag>,
    pub self_tags: im::HashSet<Tag>,
    pub dfn_range: Range<u32>,
}

impl IndexedExtra {
    pub(crate) fn match_expr(&self, expr: &Expr) -> bool {
        match expr {
            Expr::Tag(tag, _) => self.tags.contains(tag),
            Expr::Group(nodes, true) => nodes.iter().all(|it| self.match_expr(it)),
            Expr::Group(nodes, false) => nodes.iter().any(|it| self.match_expr(it)),
            Expr::Neg(node) => !self.match_expr(node),
        }
    }
}

pub(crate) struct TagGraphIndex {
    pub extras: SubjectIndexed<IndexedExtra>,
    pub subject_map: HashMap<Tag, Vec<SubjectId>>,
}

pub struct TagGraph {
    pub(crate) graph: Graph,
    pub tags: SubjectIndexed<HashSet<Tag>>,
    pub(crate) index: Option<TagGraphIndex>,
}
impl TagGraph {
    pub(crate) fn new(subject: RawSubject) -> Result<Self, GraphError> {
        let mut graph = Graph::from_raw(subject)?;
        let tags = graph
            .subjects
            .0
            .iter_mut()
            .map(|it| {
                let expr = mem::take(&mut it.expr);
                let mut tags = expr.to_tags().collect::<Result<HashSet<_>, _>>()?;
                if let Some(identity) = it.identity.clone() {
                    tags.insert(identity);
                }
                Ok(tags)
            })
            .collect::<Result<Vec<_>, _>>()?;
        Ok(Self {
            graph,
            tags: SubjectIndexed(tags),
            index: None,
        })
    }

    fn collect_ranges(
        subjects: &Subjects,
        id: SubjectId,
        mut index: u32,
        result: &mut [Range<u32>],
    ) -> u32 {
        result[id.0].start = index;
        index += 1;
        for child in &subjects[id].children {
            index = Self::collect_ranges(subjects, *child, index, result);
        }
        result[id.0].end = index;
        index
    }

    fn index_graph(&mut self) -> TagGraphIndex {
        let mut ranges = vec![0..0; self.graph.len()];
        Self::collect_ranges(&self.graph.subjects, SubjectId(0), 0, &mut ranges);

        // Parent always contains all tags from children
        let mut tags = vec![(im::HashSet::new(), im::HashSet::new()); self.graph.len()];
        for (i, subject) in self.graph.subjects.0.iter().enumerate().rev() {
            let self_tags: im::HashSet<Tag> = self.tags[subject.id].iter().cloned().collect();
            let mut all_tags = self_tags.clone();
            for child in &subject.children {
                all_tags = all_tags.union(tags[child.0].1.clone());
            }
            tags[i] = (all_tags, self_tags);
        }

        let extras = tags
            .into_iter()
            .zip(ranges)
            .map(|((tags, self_tags), range)| IndexedExtra {
                tags,
                self_tags,
                dfn_range: range,
            })
            .collect();

        let mut subject_map = HashMap::<Tag, Vec<SubjectId>>::new();
        for (subject, tags) in self.tags.0.iter().enumerate() {
            for tag in tags {
                subject_map
                    .entry(tag.clone())
                    .or_default()
                    .push(SubjectId(subject));
            }
        }

        TagGraphIndex {
            extras: SubjectIndexed(extras),
            subject_map,
        }
    }

    pub(crate) fn index(&mut self) -> &TagGraphIndex {
        if self.index.is_none() {
            self.index = Some(self.index_graph());
        }
        self.index.as_ref().unwrap()
    }
}
