""" Verify installation """
import subprocess
from typing import Tuple

import graphviz


def _run_checked(command) -> str:
    return subprocess.check_output(command, shell=True).decode("UTF-8").split("\n", maxsplit=1)[0]


def _hugo_version() -> str:
    return _run_checked("hugos version")


def _wget_version() -> str:
    return _run_checked("wgets -V")


def _graphviz_version() -> str:
    return graphviz.version()


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
    print(try_run(_hugo_version))
    print("")
    print("wget:")
    print(try_run(_wget_version))
    print("")
    print("graphviz:")
    print(try_run(_graphviz_version))
