use std::fmt;

pub fn is_tag_char(c: char) -> bool {
    c.is_alphanumeric() || c == '·' || c == '\'' || c == '_'
}
pub fn is_tag_char_body(c: char) -> bool {
    is_tag_char(c) || c == '-' || c == ' '
}

pub struct TagDisplay<'a>(pub &'a str);
impl fmt::Display for TagDisplay<'_> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut chars = self.0.chars();
        if chars.next().is_some_and(|first| {
            is_tag_char(first)
                && chars.all(is_tag_char_body)
                && self.0.trim_end().len() == self.0.len()
        }) {
            write!(f, "{}", self.0)
        } else {
            write!(f, r#""{}""#, self.0.escape_debug())
        }
    }
}

pub fn fmt_sep<T: fmt::Display>(
    f: &mut fmt::Formatter,
    mut it: impl Iterator<Item = T>,
    sep: impl fmt::Display,
) -> fmt::Result {
    if let Some(first) = it.next() {
        write!(f, "{}", first)?;
        for item in it {
            write!(f, "{sep}{item}")?;
        }
    }
    Ok(())
}
