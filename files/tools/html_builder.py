from __future__ import annotations

from typing import Iterable, Iterator

from bs4 import BeautifulSoup  # pip install beautifulsoup4
from bs4 import Tag as HtmlTag  # pip install beautifulsoup4

SOUP = BeautifulSoup(features="html.parser")
CLASS_ATTRIBUTE_NAME = "class"


def _normalize_class(c: str | Iterable[str] | None) -> list[str]:
    if c is None:
        return []
    if isinstance(c, str):
        return [c]
    return list(c)


def _join_classes(c1: str | Iterable[str] | None, c2: str | Iterable[str] | None) -> list[str]:
    return _normalize_class(c1) + _normalize_class(c2)


def new_tag(
        tag: str,
        string: str | None = None,
        class_: str | Iterable[str] | None = None,
        **kw_attributes: str | Iterable[str],
) -> HtmlTag:
    joint_classes = _join_classes(class_, kw_attributes.get(CLASS_ATTRIBUTE_NAME, None))
    if joint_classes:
        kw_attributes[CLASS_ATTRIBUTE_NAME] = joint_classes
    return SOUP.new_tag(tag, string=string, attrs=kw_attributes)


def html_to_string(tag: HtmlTag, omit_doctype: bool = False) -> str:
    doctype: str = "" if omit_doctype else "<!DOCTYPE html>"
    return doctype + str(tag)


def build_html(main_div: Iterator[HtmlTag]) -> HtmlTag:
    html_doc = new_tag("html", lang="en")
    html_head = new_tag("head")
    html_head.append(new_tag("link", rel="stylesheet", href="../tools/main.css"))
    html_head.append(new_tag("link", rel="shortcut icon", type="image/png", href="../tools/favicon.png"))
    html_head.append(new_tag("title", string="Door To Heaven"))
    html_head.append(new_tag("meta", charset="utf-8"))
    html_head.append(new_tag("meta", name="color-scheme", content="dark light"))
    html_doc.append(html_head)
    html_body = new_tag("body")
    html_body.extend(main_div)
    html_doc.append(html_body)
    return html_doc
