" test for the util module"
import os

import pytest

from odbinfo.pure.util import CommandExecutionError, chdir, run_cmd


def test_chdir_none():
    " test chdir on its default "
    cur_dir = os.getcwd()
    with chdir():
        assert os.getcwd() == cur_dir
    assert os.getcwd() == cur_dir


def test_chdir_root():
    " test chdir on its default "
    cur_dir = os.getcwd()
    with chdir("/"):
        assert os.getcwd() == "/"
    assert os.getcwd() == cur_dir


def test_run_cmd():
    " run_cmd without errors"
    run_cmd("ls")


def test_run_cmd_errors():
    " run_cmd with errors"
    with pytest.raises(CommandExecutionError):
        run_cmd("false")


def test_run_cmd_errors_no_check():
    " run_cmd with errors, but no check"
    run_cmd("false", check=False)
