""" Diagnostics module,  provides helpers for the DiagnosticsDialog"""
import os
import shlex
import subprocess
from typing import Tuple

import graphviz


def _run_checked(command: str) -> Tuple[bool, str]:
    """
    returns a tuple of boolean and string message,
    If the command succeeded the boolean is True and
    the message is the first line of command output.

    If the command failed the boolean is False and the error message."""
    try:
        return True, subprocess.check_output(
            shlex.split(command)).decode("UTF-8").split(os.linesep,
                                                        maxsplit=1)[0]
    except subprocess.CalledProcessError as error:
        return False, str(error)


def gohugo_version() -> Tuple[bool, str]:
    """ returns gohugo version"""
    return _run_checked("hugo version")


def wget_version() -> Tuple[bool, str]:
    """ returns wget version """
    return _run_checked("wget -V")


def graphviz_version() -> Tuple[bool, str]:
    """ returns graphviz version"""
    try:
        return True, ".".join(str(x) for x in graphviz.version())
    except (subprocess.CalledProcessError, RuntimeError) as error:
        return False, str(error)
