from pathlib import Path

from files import run_year

if __name__ == "__main__":
    year_dir = Path(__file__)
    run_year(year_dir.parent.name)
