from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from tools.basic_printables import Printable
from tools.html_builder import new_tag, HtmlTag
from tools.paragraph import LiteralParagraph
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class HeadLine(Printable):
    text: str = ""
    level: int = 1

    def __post_init__(self):
        if not self.text:
            raise ValueError("Empty headline.")
        if self.level <= 0:
            raise ValueError(f"Expected positive level {self.level} > 0.")

    def get_html(self) -> Iterator[HtmlTag]:
        result = new_tag(f"h{self.level}")
        result.append(self.text)
        yield result

    def get_html_monospace(self) -> Iterator[HtmlTag]:
        if self.level >= 3:
            paragraph = LiteralParagraph(text=(self.text,))
        else:
            underline = "=" if self.level == 1 else "-"
            paragraph = LiteralParagraph(text=(f"""
                {self.text}
                {underline * len(self.text)}
            """,))
        yield from paragraph.get_html()

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        underline: str | None = None
        prefix: str = ""
        match self.level:
            case 1:
                underline = "="
            case 2:
                underline = "-"
            case _:
                if not markdown_params.is_monospace:
                    prefix = "#" * self.level + " "
        result = prefix + self.text
        yield markdown_params.line_prefix + result
        if underline is not None:
            yield markdown_params.line_prefix + (underline * len(result))
