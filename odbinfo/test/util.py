" Test utils"
from pathlib import Path


def clear_generated_graphs(path: Path):
    "clear generated graphs as they depend in dot version"
    for svgfile in path.glob("**/*.gv.svg"):
        with open(svgfile, 'w', encoding='utf-8') as filehandle:
            filehandle.write('')
