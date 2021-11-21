" Test utils"
from pathlib import Path


def remove_generated_graphs(path: Path):
    "clear generated graphs as they depend in dot version"
    for svgfile in path.glob("**/*.gv.svg"):
        svgfile.unlink()
