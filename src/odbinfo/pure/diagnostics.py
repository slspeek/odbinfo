""" Diagnostics module,  provides helpers for the DiagnosticsDialog"""
import os
import shlex
import subprocess
from typing import Callable, Tuple

import graphviz


def _run_checked(command: str) -> str:
    """ Returns the first line of output from system `command`"""
    return subprocess.check_output(shlex.split(command)).decode("UTF-8").split(
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


def try_run(target: Callable[[], str]) -> Tuple[bool, str]:
    """ runs `target`
    returns a tuple of boolean and string,
    the boolean is True if the command succeeded and
    the string is the first line of command output.
    the boolean is False if the command failed and the string
    is the error message.
    """
    try:
        return True, target()
    except Exception as exception:  # pylint:disable=broad-except
        return False, str(exception)
