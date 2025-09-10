import argparse
from dataclasses import dataclass
from functools import cached_property
import os
import re
import subprocess
import sys

from tools.logger_getter import get_logger

LOGGER = get_logger(__name__)


def get_runner() -> str:
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    if sys.platform == "win32":
        return os.path.join(parent_dir, ".venv", "Scripts", "python.exe")
    else:
        return os.path.join(parent_dir, ".venv", "bin", "python")


RUNNER = get_runner()


@dataclass(frozen=True)
class ScriptsSelector:
    parent: str = "."
    directory: str = ""
    file: str = ""

    @cached_property
    def selected_directories(self) -> tuple[str, ...]:
        directory_strip = self.directory.strip()
        paths = [
            os.path.join(self.parent, entry)
            for entry in os.listdir(self.parent)
            if (
                       (not directory_strip) or (entry == directory_strip)
               ) and re.match(r"^\d{4}$", entry)
        ]
        return tuple(
            d
            for d in paths
            if os.path.isdir(d)
        )

    @cached_property
    def selected_files(self) -> tuple[str, ...]:
        file_strip = self.file.strip()
        file_strip_py = file_strip if file_strip.endswith(".py") else f"{file_strip}.py"
        directories = self.selected_directories
        paths = [
            os.path.join(directory, entry)
            for directory in directories
            for entry in os.listdir(directory)
            if (
                       (not file_strip) or (entry == file_strip_py)
               ) and (entry != "__init__.py") and entry.endswith(".py")
        ]
        return tuple(
            f
            for f in paths
            if os.path.isfile(f)
        )

    @cached_property
    def statistics(self) -> str:
        return f"Selected {len(self.selected_files)} files in {len(self.selected_directories)} directories."


def parse_arguments(*args: str) -> ScriptsSelector:
    parser = argparse.ArgumentParser(description="Run the selected scripts.")

    parser.add_argument(
        "--root-dir", type=str, default=".",
        help="Specify a root directory (default: '.')."
    )
    parser.add_argument(
        "--directory", type=str, default="",
        help="Specify a directory (default: empty string)."
             + " Empty means all directories."
    )
    parser.add_argument(
        "--file", type=str, default="",
        help="Specify a file (default: empty string)"
             + " Empty means all files."
    )

    args = parser.parse_args(args)
    return ScriptsSelector(parent=args.root_dir, directory=args.directory, file=args.file)


def run(scripts_selector: ScriptsSelector):
    LOGGER.info(scripts_selector.statistics)
    for script in scripts_selector.selected_files:
        LOGGER.info(f"Running {script} ...")
        subprocess.run([RUNNER, script], check=True)


def run_directory(fun_from_file: str):
    script_dir_full = os.path.dirname(os.path.abspath(fun_from_file))
    script_dir_base = os.path.basename(script_dir_full)
    script_dir_root = os.path.dirname(script_dir_full)
    scripts_selector = ScriptsSelector(parent=script_dir_root, directory=script_dir_base)
    run(scripts_selector)


def main(*args: str):
    scripts_selector = parse_arguments(*args)
    run(scripts_selector)


if __name__ == "__main__":
    main(*sys.argv[1:])
