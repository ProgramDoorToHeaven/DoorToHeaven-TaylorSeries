import argparse
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
import re
import subprocess
import sys

from tools.logger_getter import get_logger

LOGGER = get_logger(__name__)


def get_runner() -> Path:
    parent_dir = Path(__file__).parent.parent
    venv_dir = Path(parent_dir) / ".venv"
    if sys.platform == "win32":
        return venv_dir / "Scripts" / "python.exe"
    else:
        return venv_dir / "bin" / "python"


RUNNER = get_runner()
PARENT_DIR = Path(__file__).parent


@dataclass(frozen=True)
class DocumentsSelector:
    year: str = ""
    document: str = ""

    def __post_init__(self):
        if (self.year != "") and not self.validate_year(self.year):
            raise ValueError(f"Invalid year value '{self.year}'.")
        if (self.document != "") and not self.validate_document(self.document):
            raise ValueError(f"Invalid document value '{self.document}'.")

    @staticmethod
    def validate_year(year: str) -> bool:
        return bool(re.match(r"^\d{4}$", year))

    @staticmethod
    def validate_document(document: str) -> bool:
        return bool(re.match(r"^\d{8}_\d{8}_", document))

    @cached_property
    def selected_years(self) -> tuple[Path, ...]:
        if self.year:
            # one year selected
            year_dir = PARENT_DIR / self.year
            if year_dir.is_dir():
                return (year_dir,)
            return ()

        return tuple(
            year_dir
            for year_dir in PARENT_DIR.iterdir()
            if year_dir.is_dir()
            if self.validate_year(year_dir.name)
        )

    @cached_property
    def selected_documents(self) -> tuple[Path, ...]:
        if self.document:
            # one document selected
            return tuple(
                document_dir
                for year_dir in self.selected_years
                if (document_dir := year_dir / self.document).is_dir()
            )

        return tuple(
            document_dir
            for year_dir in self.selected_years
            for document_dir in year_dir.iterdir()
            if document_dir.is_dir()
            if self.validate_document(document_dir.name)
        )

    @cached_property
    def statistics(self) -> str:
        return f"Selected {len(self.selected_documents)} documents in {len(self.selected_years)} years."


def parse_arguments(*args: str) -> DocumentsSelector:
    parser = argparse.ArgumentParser(description="Run the selected scripts.")

    parser.add_argument(
        "--year", type=str, default="",
        help="Specify a year (default: empty string)."
             + " Empty means all years."
    )
    parser.add_argument(
        "--document", type=str, default="",
        help="Specify a document (default: empty string)"
             + " Empty means all document."
    )

    args = parser.parse_args(args)
    return DocumentsSelector(year=args.year, document=args.document)


def run(scripts_selector: DocumentsSelector):
    LOGGER.info(scripts_selector.statistics)
    for document in scripts_selector.selected_documents:
        LOGGER.info(f"Running {document} ...")
        subprocess.run([RUNNER, document / "__init__.py"], check=True)
    LOGGER.info("Finished running documents.")


def run_year(year: str):
    run(DocumentsSelector(year=year))


def main(*args: str):
    scripts_selector = parse_arguments(*args)
    run(scripts_selector)


if __name__ == "__main__":
    main(*sys.argv[1:])
