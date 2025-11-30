from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from typing import Iterable, Iterator

from tools.html_builder import HtmlTag, new_tag


@dataclass(frozen=True)
class PageBlockTypeItem:
    html_tag: str = "div"
    html_classes: tuple[str, ...] = ()
    markdown_start: str | None = None
    markdown_end: str | None = None
    markdown_each_line_prefix: str = ""

    @cached_property
    def is_markdown_code_block(self) -> bool:
        return self.markdown_end == '```'

    def get_html_tag(self, contents: Iterable[HtmlTag | str]) -> Iterator[HtmlTag]:
        wrapper = new_tag("div", class_=self.html_classes)
        text: list[str] = []

        def flush_text_if_nonempty() -> None:
            if not text:
                return
            text_element = new_tag(self.html_tag)
            text_element.extend(text)
            wrapper.append(text_element)
            text.clear()

        for part in contents:
            if isinstance(part, str):
                if text or part != "\n":
                    text.append(part)
                else:
                    wrapper.append(part)
            elif isinstance(part, HtmlTag):
                flush_text_if_nonempty()
                wrapper.append(part)
        flush_text_if_nonempty()
        yield wrapper


class PageBlockType(Enum):
    THOUGHTS = PageBlockTypeItem(
        html_classes=("thoughts",),
    )
    TYPEWRITER = PageBlockTypeItem(
        html_classes=("typewriter",),
        markdown_start="```", markdown_end="```",
    )
    QUOTATION = PageBlockTypeItem(
        html_classes=("quotation",),
        markdown_each_line_prefix="> ",
    )

    def get_html_tag(self, contents: Iterable[HtmlTag | str]) -> Iterator[HtmlTag]:
        return self.value.get_html_tag(contents)
