use serde::{Deserialize, Serialize};
use std::{collections::HashMap, sync::Arc};

use crate::{GraphError, Query, SubjectId, Tag, TagGraph};

pub struct Implication {
    pub condition: Vec<Tag>,
    pub consequence: Vec<Tag>,
}

#[derive(Clone, Serialize, Deserialize)]
enum SubjectUpdate {
    Tag(Tag),
    Identity(Tag),
}

#[derive(Default, Serialize, Deserialize)]
pub struct Patch {
    tags: Vec<(SubjectId, Tag)>,
    identities: Vec<(SubjectId, Tag)>,
}
impl Patch {
    pub fn is_empty(&self) -> bool {
        self.tags.is_empty() && self.identities.is_empty()
    }

    pub fn apply_to(&self, graph: &mut TagGraph) {
        for (id, tag) in self.tags.iter().cloned() {
            graph.tags[id].insert(tag);
        }
        if let Some(index) = &mut graph.index {
            for (id, tag) in self.tags.iter().chain(self.identities.iter()) {
                let mut current = *id;
                loop {
                    index.extras[current].tags.insert(tag.clone());
                    if current == SubjectId(0) {
                        break;
                    }
                    current = graph.graph.subjects[current].parent;
                }
            }
            for (id, identity) in self.identities.iter().cloned() {
                index.subject_map.entry(identity).or_default().push(id);
            }
        }
    }
}

#[derive(Default)]
pub struct PostProcessor {
    definitions: HashMap<Tag, Arc<Query>>,
    implications: HashMap<Tag, Arc<Implication>>,
}
impl PostProcessor {
    pub fn add_definition(&mut self, tag: Tag, query: impl Into<Arc<Query>>) {
        self.definitions.insert(tag, query.into());
    }
    pub fn remove_definition(&mut self, tag: &str) {
        self.definitions.remove(tag);
    }
    pub fn get_definition(&self, tag: &str) -> Option<&Arc<Query>> {
        self.definitions.get(tag)
    }

    pub fn add_implication(&mut self, implication: impl Into<Arc<Implication>>) {
        let implication = implication.into();
        self.implications
            .insert(implication.condition[0].clone(), implication);
    }
    pub fn remove_implication(&mut self, implication: &Implication) {
        self.implications.remove(&implication.condition[0]);
    }

    pub fn make_patch(&self, graph: &mut TagGraph) -> Result<Patch, GraphError> {
        let mut result = Patch::default();
        // TODO: optimize this
        for (tag, definition) in &self.definitions {
            for a_match in definition.all_matches(graph) {
                if graph.tags[a_match].insert(tag.clone()) {
                    result.tags.push((a_match, tag.clone()));
                }
            }
        }

        for subject in &mut graph.graph.subjects.0 {
            let tags = &graph.tags[subject.id];
            let implications = tags
                .iter()
                .filter_map(|it| self.implications.get(it))
                .collect::<Vec<_>>();

            for implication in implications {
                let graph_tags = &mut graph.tags[subject.id];
                result.tags.extend(
                    implication
                        .consequence
                        .iter()
                        .filter(|it| graph_tags.insert(Arc::clone(it)))
                        .map(|it| (subject.id, it.clone())),
                );
            }
        }

        Ok(result)
    }
}
