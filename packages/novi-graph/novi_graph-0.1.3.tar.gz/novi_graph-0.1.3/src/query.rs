use im::HashSet;
use serde::Serialize;
use std::{fmt, ops::Range};

use crate::{
    utils::{fmt_sep, TagDisplay},
    Graph, GraphError, GraphErrorKind, RawSubject, Relation, SubjectId, SubjectRef, Tag, TagGraph,
    TagGraphIndex,
};

#[derive(Debug, Serialize)]
pub struct MetaQuery {
    pub neg: bool,
    pub kind: Tag,
    pub args: Vec<SubjectRef>,
    pub span: Range<usize>,
}

impl fmt::Display for MetaQuery {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[")?;
        if self.neg {
            write!(f, "-")?;
        }
        write!(f, "{}:", TagDisplay(&self.kind))?;
        fmt_sep(f, self.args.iter(), ", ")?;
        write!(f, "]")
    }
}

pub struct Query {
    pub(crate) graph: Graph,
    pub(crate) meta_queries: Vec<MetaQuery>,
    unique_groups: Vec<Vec<SubjectId>>,
    inline: bool,
}
impl Query {
    pub(crate) fn new(
        subject: RawSubject,
        mut meta_queries: Vec<MetaQuery>,
        inline: bool,
    ) -> Result<Self, GraphError> {
        let graph = Graph::from_raw(subject)?;
        let mut unique_groups = vec![];
        let mut err = None;
        meta_queries.retain(|it| {
            if it.kind.as_ref() != "unique" {
                return true;
            }
            if it.neg {
                err = Some(
                    GraphErrorKind::InvalidMetaQuery(
                        "unique constraint cannot be negated".to_owned(),
                    )
                    .with_span(it.span.clone()),
                );
                return false;
            }
            let mut group = vec![];
            for arg in &it.args {
                match graph.resolve(arg) {
                    Ok(subject) => {
                        group.push(subject);
                    }
                    Err(e) => {
                        err = Some(e);
                        return false;
                    }
                }
            }
            unique_groups.push(group);
            false
        });

        Ok(Self {
            graph,
            meta_queries,
            unique_groups,
            inline,
        })
    }

    pub fn meta_queries(&self) -> &[MetaQuery] {
        &self.meta_queries
    }

    fn alternatves<'s>(
        &'s self,
        graph: &'s Graph,
        index: &'s TagGraphIndex,
        choices: &[SubjectId],
        id: SubjectId,
        allow_any: bool,
    ) -> Option<impl Iterator<Item = SubjectId> + 's> {
        let query_subject = &self.graph.subjects[id];
        let parent = &graph.subjects[choices[query_subject.parent.0]];
        let search_range = if allow_any {
            0..graph.len()
        } else {
            let range = &index.extras[parent.id].dfn_range;
            (range.start as usize + 1)..range.end as usize
        };

        Some(search_range.map(SubjectId).filter_map(move |id| {
            let alt = &graph.subjects[id];
            if !index.extras[alt.id].match_expr(&query_subject.expr)
                || query_subject
                    .identity
                    .as_ref()
                    .is_some_and(|it| !index.extras[alt.id].self_tags.contains(it))
                || alt.relation.is_some() != query_subject.relation.is_some()
            {
                return None;
            }
            Some(alt.id)
        }))
    }

    // TODO: optimize
    fn search(
        &self,
        graph: &Graph,
        index: &TagGraphIndex,
        id: SubjectId,
        choices: &mut [SubjectId],
        allow_any: bool,
    ) -> bool {
        if id.0 == self.graph.len() {
            for group in &self.unique_groups {
                let mut set = HashSet::new();
                for &subject in group {
                    if set.insert(choices[subject.0]).is_some() {
                        return false;
                    }
                }
            }

            // Now check relations
            for subject in &self.graph.subjects.0 {
                let Some(Relation { source, target }) = &subject.relation else {
                    continue;
                };
                let choice = &graph.subjects[choices[subject.id.0]];
                let Some(choice_rel) = &choice.relation else {
                    unreachable!()
                };
                // TODO: Eliminate this kind of wrong match early
                if choice_rel.source != choices[source.0] || choice_rel.target != choices[target.0]
                {
                    return false;
                }
            }
            return true;
        }
        let Some(alts) = self.alternatves(graph, index, choices, id, allow_any) else {
            return false;
        };
        for alt in alts {
            choices[id.0] = alt;
            if self.search(graph, index, SubjectId(id.0 + 1), choices, false) {
                return true;
            }
        }

        false
    }

    pub fn is_match(&self, graph: &mut TagGraph) -> bool {
        graph.index();
        let index = graph.index.as_ref().unwrap();
        let graph = &graph.graph;
        if !index.extras[SubjectId(0)].match_expr(&self.graph.root().expr) {
            return false;
        }

        let mut choices = vec![SubjectId(0); self.graph.len()];
        self.search(graph, index, SubjectId(1), &mut choices, self.inline)
    }

    pub fn all_matches(&self, graph: &mut TagGraph) -> HashSet<SubjectId> {
        assert!(self.inline && self.graph.len() >= 2);

        graph.index();
        let index = graph.index.as_ref().unwrap();
        let graph = &graph.graph;

        let mut skipped = HashSet::new();
        let mut result = HashSet::new();
        let mut choices = vec![SubjectId(0); self.graph.len()];
        let Some(alts) = self.alternatves(graph, index, &choices, SubjectId(1), true) else {
            return result;
        };

        for alt in alts {
            if skipped.contains(&alt) {
                continue;
            }
            choices[1] = alt;
            if self.search(graph, index, SubjectId(2), &mut choices, false) {
                let mut x = alt;
                while x.0 != 0 {
                    let parent = graph.subjects[x].parent;
                    if skipped.insert(parent).is_some() {
                        break;
                    }
                    result.remove(&parent);
                    x = parent;
                }
                result.insert(alt);
            }
        }
        result
    }
}
