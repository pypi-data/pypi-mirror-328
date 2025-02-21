use pyo3::{prelude::*, types::PyList};

use crate::{Expr, Query};

fn bind_arg<'py, T: IntoPyObject<'py>>(args: &Bound<'py, PyList>, value: T) -> PyResult<String> {
    args.append(value)?;
    Ok(format!("${}", args.len()))
}

fn into_generic(expr: Expr) -> Expr {
    match expr {
        Expr::Tag(tag, span) => Expr::Tag(tag, span),
        Expr::Group(nodes, ands) => {
            let mut new_nodes = Vec::with_capacity(nodes.len());
            for node in nodes {
                let node = into_generic(node);
                if node.is_any() {
                    if !ands {
                        return Expr::default();
                    }
                } else {
                    new_nodes.push(node);
                }
            }
            Expr::concat(new_nodes, ands)
        }
        Expr::Neg(_) => Expr::default(),
    }
}

fn join_clauses<S>(clauses: &[S], ands: bool) -> String
where
    S: AsRef<str>,
{
    if clauses.is_empty() {
        return if ands { "true" } else { "false" }.to_owned();
    }
    if clauses.len() == 1 {
        return clauses[0].as_ref().to_owned();
    }

    let join = if ands { " and " } else { " or " };
    let mut clause = format!("({}", clauses[0].as_ref());
    for other in &clauses[1..] {
        clause += join;
        clause += other.as_ref();
    }
    clause.push(')');
    clause
}

fn expr_to_sql<'py>(py: Python<'py>, expr: &Expr, args: &Bound<PyList>) -> PyResult<String> {
    Ok(match expr {
        Expr::Tag(tag, _) => format!("(tags @> array[{}])", bind_arg(args, tag.as_ref())?),
        Expr::Group(nodes, ands) => {
            let mut plain_tags = vec![];
            let mut others = vec![];
            for node in nodes {
                match node {
                    Expr::Tag(tag, _) => plain_tags.push(tag.as_ref()),
                    _ => others.push(expr_to_sql(py, node, args)?),
                }
            }
            if !plain_tags.is_empty() {
                let op = if *ands { "@>" } else { "&&" };
                others.push(format!("(tags {op} {})", bind_arg(args, plain_tags)?));
            }
            join_clauses(&others, *ands)
        }
        Expr::Neg(expr) => format!("NOT {}", expr_to_sql(py, expr, args)?),
    })
}

pub fn to_sql<'py>(py: Python<'py>, query: &Query, args: Bound<PyList>) -> PyResult<String> {
    let mut fuzzy_nodes = vec![query.graph.root().expr.clone()];
    for subject in query.graph.subjects.0.iter().skip(1) {
        if let Some(identity) = subject.identity.clone() {
            fuzzy_nodes.push(Expr::Tag(identity, 0..0));
        }
        fuzzy_nodes.push(subject.expr.clone());
    }
    let clause = expr_to_sql(py, &into_generic(Expr::Group(fuzzy_nodes, true)), &args)?;

    Ok(clause)
}
