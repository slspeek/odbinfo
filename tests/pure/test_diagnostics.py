""" test for diagnostics module """
import subprocess
from unittest.mock import patch

import graphviz

from odbinfo.pure import diagnostics


def test__run_checked_success():
    assert diagnostics._run_checked("bash -c 'echo Hello; exit 0'") == (
        True, "Hello")


def test__run_checked_failure():
    assert diagnostics._run_checked("bash -c 'exit 1'") == (
        False,
        "Command '['bash', '-c', 'exit 1']' returned non-zero exit status 1.")


def test_grahviz_version():
    assert diagnostics.graphviz_version()


def test_grahviz_version_fail():
    with patch.object(graphviz,
                      "version",
                      side_effect=subprocess.CalledProcessError(cmd="fail",
                                                                returncode=1)):
        assert diagnostics.graphviz_version() == (
            False, "Command 'fail' returned non-zero exit status 1.")

    with patch.object(graphviz, "version", side_effect=RuntimeError("Boom")):
        assert diagnostics.graphviz_version() == (False, "Boom")
