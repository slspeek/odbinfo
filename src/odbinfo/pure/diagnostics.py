""" Verify installation """
import subprocess
from typing import Tuple

import graphviz


def _run_checked(command) -> str:
    return subprocess.check_output(command, shell=True).decode("UTF-8").split(
        "\n", maxsplit=1)[0]


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


def verify_installation():
    """ print versions of required components """
    print("ODBInfo verify installation:")
    print("")
    print("Hugo:")
    print(try_run(gohugo_version))
    print("")
    print("wget:")
    print(try_run(wget_version))
    print("")
    print("graphviz:")
    print(try_run(graphviz_version))
