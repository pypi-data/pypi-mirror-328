use js_sys::Array;
use serde::Serialize;
use serde_wasm_bindgen::to_value;
use std::str;
use wasm_bindgen::prelude::*;

use crate::{graph, parse, postprocess, query, tag_graph, Relation, Tag};

// For mysterical reason we can't use js_name since it will produce wrong .d.ts
#[wasm_bindgen]
pub struct Query(query::Query);

#[wasm_bindgen]
impl Query {
    #[wasm_bindgen(js_name = "isMatch")]
    pub fn is_match(&self, graph: &mut TagGraph) -> bool {
        self.0.is_match(&mut graph.0)
    }

    #[wasm_bindgen(js_name = "metaQueries")]
    pub fn meta_queries(&self) -> Result<JsValue, serde_wasm_bindgen::Error> {
        to_value(&self.0.meta_queries)
    }
}

#[derive(Serialize)]
struct PlainError {
    message: String,
    from: usize,
    to: usize,
}

fn convert_error(e: graph::GraphError) -> JsError {
    let error = PlainError {
        message: e.to_string(),
        from: e.span.start,
        to: e.span.end,
    };
    JsError::new(&serde_json::to_string(&error).unwrap())
}

#[wasm_bindgen(js_name = "parseQuery")]
pub fn parse_query(query: &str, inline: Option<bool>) -> Result<Query, JsError> {
    parse::parse_query(query, inline.unwrap_or(false))
        .map(Query)
        .map_err(convert_error)
}

#[derive(Serialize)]
struct PlainSubject {
    id: u32,
    parent: u32,
    name: Option<String>,
    identity: Option<String>,
    tags: Vec<String>,
}
#[derive(Serialize)]
struct PlainRelation {
    edge: u32,
    source: u32,
    target: u32,
}

#[wasm_bindgen]
pub struct Patch(postprocess::Patch);
#[wasm_bindgen]
impl Patch {
    pub fn parse(encoded: &str) -> Result<Patch, JsError> {
        use base64::prelude::*;
        let bytes = BASE64_STANDARD.decode(encoded.as_bytes()).unwrap();
        serde_cbor::from_slice(&bytes)
            .map(Patch)
            .map_err(|e| JsError::new(&e.to_string()))
    }

    #[wasm_bindgen(js_name = "applyTo")]
    pub fn apply_to(&self, graph: &mut TagGraph) {
        self.0.apply_to(&mut graph.0);
    }
}

#[wasm_bindgen]
pub struct TagGraph(tag_graph::TagGraph);

#[wasm_bindgen]
impl TagGraph {
    pub fn serialize(
        &self,
        subjects: &Array,
        relations: &Array,
    ) -> Result<(), serde_wasm_bindgen::Error> {
        for subject in self.0.graph.subjects.0.iter() {
            subjects.push(&to_value(&PlainSubject {
                id: subject.id.0 as u32,
                parent: subject.parent.0 as u32,
                name: subject.name.as_ref().map(Tag::to_string),
                identity: subject.identity.as_ref().map(Tag::to_string),
                tags: self.0.tags[subject.id]
                    .iter()
                    .map(|it| it.to_string())
                    .collect(),
            })?);
            if let Some(Relation { source, target }) = &subject.relation {
                relations.push(&to_value(&PlainRelation {
                    edge: subject.id.0 as u32,
                    source: source.0 as u32,
                    target: target.0 as u32,
                })?);
            }
        }
        Ok(())
    }
}

#[wasm_bindgen(js_name = "parseTagGraph")]
pub fn parse_tag_graph(graph: &str) -> Result<TagGraph, JsError> {
    parse::parse_tag_graph(graph)
        .map(TagGraph)
        .map_err(convert_error)
}

#[wasm_bindgen]
pub fn format(graph: &str) -> Result<String, JsError> {
    parse::parse_raw(graph)
        .map(|it| it.to_string())
        .map_err(convert_error)
}
