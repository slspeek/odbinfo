""" test for the util module"""
import os
import subprocess

import pytest

from odbinfo.pure.util import chdir, run_cmd


def test_chdir_none():
    """ test chdir on its default """
    cur_dir = os.getcwd()
    with chdir():
        assert os.getcwd() == cur_dir
    assert os.getcwd() == cur_dir


def test_chdir_root():
    """ test chdir on its default """
    cur_dir = os.getcwd()
    with chdir("/"):
        assert os.getcwd() == "/"
    assert os.getcwd() == cur_dir


def test_run_cmd():
    """ run_cmd without errors"""
    run_cmd("ls")


def test_run_cmd_errors():
    """ run_cmd with errors"""
    with pytest.raises(subprocess.CalledProcessError):
        run_cmd("false")


def test_run_cmd_errors_verify_stderr(caplog):
    """ run_cmd with errors, but no check"""
    run_cmd("bash -c 'echo errorout 1>&2;false'", check=False)
    assert caplog.records[
        0].message == "System command: bash -c 'echo errorout 1>&2;false' failed (returncode=1)"
    assert caplog.records[1].message == "Output: errorout\n"


def test_run_cmd_errors_verify_stdout(caplog):
    """ run_cmd with errors, but no check"""
    run_cmd("bash -c 'echo stdout;false'", check=False)
    assert caplog.records[
        0].message == "System command: bash -c 'echo stdout;false' failed (returncode=1)"
    assert caplog.records[1].message == "Output: stdout\n"
