""" Verify installation """
import os
import subprocess
from typing import Tuple

import graphviz


def _run_checked(command) -> str:
    return subprocess.check_output(command, shell=True).decode("UTF-8").split(
        os.linesep, maxsplit=1)[0]


def gohugo_version() -> str:
    """ returns gohugo version"""
    return _run_checked("hugo version")


def wget_version() -> str:
    """ returns wget version """
    return _run_checked("wget -V")


def graphviz_version() -> str:
    """ returns graphviz version"""
    return ".".join(str(x) for x in graphviz.version())


def try_run(target) -> Tuple[bool, str]:
    """ runs `target` """
    try:
        return True, target()
    except Exception as exception:  # pylint:disable=broad-except
        return False, str(exception)
