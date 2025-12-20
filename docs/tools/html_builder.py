from __future__ import annotations

from typing import Iterable, Iterator

from bs4 import BeautifulSoup  # pip install beautifulsoup4
from bs4 import Tag as HtmlTag  # pip install beautifulsoup4

SOUP = BeautifulSoup(features="html.parser")
CLASS_ATTRIBUTE_NAME = "class"


def _normalize_class(c: str | Iterable[str] | None) -> set[str]:
    if c is None:
        return set()
    if isinstance(c, str):
        return {c}
    return set(c)


def _join_classes(
        c1: str | Iterable[str] | None,
        c2: str | Iterable[str] | None,
        omit_space_before: bool = False,
) -> list[str]:
    omit_space_class: str | None = "omit_space_before" if omit_space_before else None
    return list(_normalize_class(c1) | _normalize_class(c2) | _normalize_class(omit_space_class))


def new_tag(
        tag: str,
        string: str | None = None,
        class_: str | Iterable[str] | None = None,
        omit_space_before: bool = False,
        **kw_attributes: str | Iterable[str],
) -> HtmlTag:
    joint_classes = _join_classes(
        class_,
        kw_attributes.get(CLASS_ATTRIBUTE_NAME, None),
        omit_space_before=omit_space_before,
    )
    if joint_classes:
        kw_attributes[CLASS_ATTRIBUTE_NAME] = joint_classes
    return SOUP.new_tag(tag, string=string, attrs=kw_attributes)


def html_to_string(tag: HtmlTag, omit_doctype: bool = False) -> str:
    doctype: str = "" if omit_doctype else "<!DOCTYPE html>"
    return doctype + str(tag)


def build_html(
        main_div: Iterator[HtmlTag],
        levels_up_to_tools_parent: int = 2,
) -> HtmlTag:
    tools_directory = ("../" * levels_up_to_tools_parent) + "tools"
    html_doc = new_tag("html", lang="en")
    html_head = new_tag("head")
    html_head.append(new_tag("link", rel="stylesheet", href=f"{tools_directory}/main.css"))
    html_head.append(new_tag("link", rel="shortcut icon", type="image/png", href=f"{tools_directory}/favicon.png"))
    html_head.append(new_tag("title", string="Door To Heaven"))
    html_head.append(new_tag("meta", charset="utf-8"))
    html_head.append(new_tag("meta", name="color-scheme", content="dark light"))
    html_head.append(new_tag("meta", name="viewport", content="width=device-width, initial-scale=1.0"))
    html_doc.append(html_head)
    html_body = new_tag("body")
    html_body.extend(main_div)
    html_doc.append(html_body)
    return html_doc
