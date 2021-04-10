" Verify installation "
import subprocess

import graphviz


def _run_checked(command) -> str:
    cprocess = subprocess.run(command,
                              shell=True,
                              capture_output=True,
                              check=True)
    return cprocess.stdout.decode('UTF-8')


def _hugo_version() -> str:
    return _run_checked("hugo version")


def _wget_version() -> str:
    return _run_checked("wget -V")


def _graphviz_version() -> str:
    return graphviz.version()


def verify_installation():
    " print versions of required components "
    print("ODBInfo verify installation:")
    print("")
    print("Hugo:")
    print(_hugo_version())
    print("")
    print("wget:")
    print(_wget_version())
    print("")
    print("graphviz:")
    print(_graphviz_version())
