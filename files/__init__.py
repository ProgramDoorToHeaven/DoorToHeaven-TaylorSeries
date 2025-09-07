import os
import re
import subprocess
import sys

from tools.logger_getter import get_logger

LOGGER = get_logger(__name__)

if sys.platform == "win32":
    RUNNER = os.path.join("..", ".venv", "Scripts", "python.exe")
else:
    RUNNER = os.path.join("..", ".venv", "bin", "python")


def render_all(root_dir):
    for dir_path, _, files in os.walk(root_dir):
        dir_name = os.path.basename(os.path.normpath(dir_path))
        if not re.match(r"^\d{4}$", dir_name):
            LOGGER.info(f"Skipping directory {dir_name}")
            continue
        for file in files:
            if not file.endswith(".py"):
                continue
            file_path = os.path.join(dir_path, file)
            if not re.match(r"^\d{8}_", file):
                LOGGER.info(f"Skipping file {file_path}")
                continue
            LOGGER.info(f"Running {file_path} ...")
            subprocess.run([RUNNER, file_path], check=True)


if __name__ == "__main__":
    root_directory = "."
    render_all(root_directory)
