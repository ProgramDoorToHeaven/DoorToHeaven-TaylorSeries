from __future__ import annotations

from typing import Iterable

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
    kw_attributes[CLASS_ATTRIBUTE_NAME] = _join_classes(class_, kw_attributes.get(CLASS_ATTRIBUTE_NAME, None))
    return SOUP.new_tag(tag, string=string, **kw_attributes)


def html_to_string(tag: HtmlTag) -> str:
    return str(tag)
