mod sql;

use pyo3::{exceptions::PyValueError, prelude::*, types::PyList};
use std::sync::Arc;

use crate::{parse, Implication, Patch, PostProcessor, Query, SubjectId, Tag, TagGraph};

fn convert_error(e: crate::GraphError) -> PyErr {
    PyValueError::new_err(e.to_string())
}

#[pyclass(name = "Query")]
struct QueryWrapper(Arc<Query>);
#[pymethods]
impl QueryWrapper {
    fn is_match(self_: PyRef<Self>, graph: &mut TagGraphWrapper) -> PyResult<bool> {
        Ok(self_.0.is_match(&mut graph.0))
    }

    fn to_sql(self_: PyRef<Self>, args: Bound<PyList>) -> PyResult<String> {
        sql::to_sql(self_.py(), &self_.0, args)
    }

    fn meta_queries(self_: PyRef<Self>) -> PyResult<Vec<(bool, String, Bound<PyList>)>> {
        self_
            .0
            .meta_queries
            .iter()
            .map(|it| {
                let list = PyList::empty(self_.py());
                for arg in &it.args {
                    if arg.path.len() > 1 {
                        list.append(arg.path.iter().map(Tag::to_string).collect::<Vec<_>>())?;
                    } else {
                        list.append(arg.path[0].to_string())?;
                    }
                }
                Ok((it.neg, it.kind.to_string(), list))
            })
            .collect()
    }
}

#[pyclass(name = "Implication")]
struct ImplicationWrapper(Arc<Implication>);
#[pymethods]
impl ImplicationWrapper {
    #[new]
    #[pyo3(signature = (condition, consequence))]
    fn new(condition: Vec<String>, consequence: Vec<String>) -> Self {
        ImplicationWrapper(Arc::new(Implication {
            condition: condition.into_iter().map(Into::into).collect(),
            consequence: consequence.into_iter().map(Into::into).collect(),
        }))
    }
}

#[pyclass(name = "TagGraph")]
struct TagGraphWrapper(TagGraph);
#[pymethods]
impl TagGraphWrapper {
    fn collect_tags(mut self_: PyRefMut<Self>) -> PyResult<Vec<String>> {
        let tags = &self_.0.index().extras[SubjectId(0)].tags;
        Ok(tags.iter().map(|it| it.to_string()).collect())
    }
}

#[pyclass(name = "Patch")]
struct PatchWrapper(Patch);
#[pymethods]
impl PatchWrapper {
    fn is_empty(self_: PyRef<Self>) -> bool {
        self_.0.is_empty()
    }

    fn to_bytes(self_: PyRef<Self>) -> Vec<u8> {
        serde_cbor::ser::to_vec_packed(&self_.0).unwrap()
    }

    #[staticmethod]
    fn from_bytes(bytes: Vec<u8>) -> Self {
        serde_cbor::from_slice(&bytes).map(Self).unwrap()
    }

    fn apply_to(self_: PyRef<Self>, graph: &mut TagGraphWrapper) {
        self_.0.apply_to(&mut graph.0);
    }
}

#[pyclass(name = "PostProcessor")]
struct PostProcessorWrapper(PostProcessor);
#[pymethods]
impl PostProcessorWrapper {
    #[new]
    fn new() -> Self {
        PostProcessorWrapper(PostProcessor::default())
    }

    fn add_definition(mut self_: PyRefMut<Self>, tag: &str, query: &QueryWrapper) {
        self_.0.add_definition(tag.into(), query.0.clone());
    }
    fn remove_definition(mut self_: PyRefMut<Self>, tag: &str) {
        self_.0.remove_definition(tag);
    }
    fn get_definition(self_: PyRef<Self>, tag: &str) -> Option<QueryWrapper> {
        self_
            .0
            .get_definition(tag)
            .map(Arc::clone)
            .map(QueryWrapper)
    }

    fn add_implication(mut self_: PyRefMut<Self>, implication: &ImplicationWrapper) {
        self_.0.add_implication(implication.0.clone());
    }
    fn remove_implication(mut self_: PyRefMut<Self>, implication: &ImplicationWrapper) {
        self_.0.remove_implication(&implication.0);
    }

    fn make_patch(self_: PyRef<Self>, graph: &mut TagGraphWrapper) -> PyResult<PatchWrapper> {
        self_
            .0
            .make_patch(&mut graph.0)
            .map(PatchWrapper)
            .map_err(convert_error)
    }
}

#[pyfunction]
fn parse_tag_graph(graph: &str) -> PyResult<TagGraphWrapper> {
    parse::parse_tag_graph(graph)
        .map(TagGraphWrapper)
        .map_err(convert_error)
}

#[pyfunction]
#[pyo3(signature = (query, inline = false))]
fn parse_query(query: &str, inline: bool) -> PyResult<QueryWrapper> {
    parse::parse_query(query, inline)
        .map(Arc::new)
        .map(QueryWrapper)
        .map_err(convert_error)
}

#[pyfunction]
fn parse_implication(implication: &str) -> PyResult<ImplicationWrapper> {
    parse::parse_implication(implication)
        .map(Arc::new)
        .map(ImplicationWrapper)
        .map_err(convert_error)
}

#[pymodule]
fn novi_graph(m: &Bound<PyModule>) -> PyResult<()> {
    m.add_class::<TagGraphWrapper>()?;
    m.add_class::<QueryWrapper>()?;
    m.add_class::<ImplicationWrapper>()?;
    m.add_class::<PatchWrapper>()?;
    m.add_class::<PostProcessorWrapper>()?;
    m.add_function(wrap_pyfunction!(parse_tag_graph, m)?)?;
    m.add_function(wrap_pyfunction!(parse_query, m)?)?;
    m.add_function(wrap_pyfunction!(parse_implication, m)?)?;
    Ok(())
}
