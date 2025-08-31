from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Iterator

from tools.html_builder import HtmlTag, new_tag


@dataclass(frozen=True)
class PageBlockTypeItem:
    html_tag: str
    html_classes: tuple[str, ...] = ()
    markdown_start: str | None = None
    markdown_end: str | None = None
    markdown_each_line_prefix: str = ""

    def get_html_tag(self, contents: Iterable[HtmlTag | str]) -> Iterator[HtmlTag]:
        result = new_tag(self.html_tag)
        result.extend(contents)
        wrapper = new_tag("div", class_=self.html_classes)
        wrapper.append(result)
        yield wrapper


class PageBlockType(Enum):
    THOUGHTS = PageBlockTypeItem(
        html_tag="div", html_classes=("thoughts",),
    )
    TYPEWRITER = PageBlockTypeItem(
        html_tag="pre", html_classes=("typewriter",),
        markdown_start="```", markdown_end="```",
    )
    QUOTATION = PageBlockTypeItem(
        html_tag="div", html_classes=("quotation",),
        markdown_each_line_prefix="> ",
    )

    def get_html_tag(self, contents: Iterable[HtmlTag | str]) -> Iterator[HtmlTag]:
        return self.value.get_html_tag(contents)

