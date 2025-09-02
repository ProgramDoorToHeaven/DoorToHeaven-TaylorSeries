from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from tools.basic_printables import Printable
from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class Image(Printable):
    relative_path: str = ""
    alternative_text: str = ""

    @cached_property
    def alternative_text_or_rel_path(self):
        return self.alternative_text or self.relative_path

    def __post_init__(self):
        if self.relative_path == "":
            raise ValueError("Empty relative path.")

    def get_html(self) -> Iterator[HtmlTag]:
        yield new_tag(
            "img",
            src=self.relative_path,
            alt=self.alternative_text_or_rel_path,
        )

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        if markdown_params.is_monospace:
            raise NotImplementedError("Images are not supported inside monospace blocks.")
        prefix: str = markdown_params.get_line_prefix(0, first_line_special_prefix)
        yield f"{prefix}![{self.alternative_text_or_rel_path}]({self.relative_path})"
