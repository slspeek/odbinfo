" tests for the writer"
import os
import webbrowser
from pathlib import Path
from unittest.mock import patch

import pytest
from graphviz import Digraph

from odbinfo.pure.writer import (_open_browser, _write_graphs, chdir,
                                 clean_old_site, new_site, run_cmd)
from odbinfo.test.resource import TEST_OUTPUT_TPL


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


def test_clean_old_site(tmpdir):
    " test cleaning old site "
    os.makedirs(tmpdir / "exampledb")
    os.makedirs(tmpdir / "exampledb-local")
    clean_old_site(Path(tmpdir), "exampledb")


@pytest.mark.slow
def test_write_graphs(tmpdir, monkeypatch):
    "test write graphs"
    monkeypatch.chdir(tmpdir)
    graph = Digraph()

    # pylint:disable=too-few-public-methods
    class Meta:
        "for test only"
        graphs = []

    obj = Meta()
    obj.graphs = [graph]
    _write_graphs(obj)


@pytest.mark.slow
def test_new_site():
    """ test new site scaffolding """
    new_site(TEST_OUTPUT_TPL.format(""), "test-site")
    assert os.path.exists(TEST_OUTPUT_TPL.format("test-site"))


def test_open_browser():
    " test the _open_browser function "
    with patch.object(webbrowser, 'open') as openmock:
        with patch.object(os, 'getcwd', return_value="/home"):
            with patch.object(os, 'getenv', return_value="0"):
                _open_browser("site")
    openmock.assert_called_with("file:///home/site/index.html")


def test_open_browser_nop():
    " test the _open_browser function doing nothing"
    with patch.object(webbrowser, 'open') as openmock:
        with patch.object(os, 'getcwd', return_value="/home"):
            with patch.object(os, 'getenv', return_value="1"):
                _open_browser("site")
    openmock.assert_not_called()


def test_run_cmd():
    " run_cmd without errors"
    run_cmd("ls", error_mesg="ERROR command ls failed")


def test_run_cmd_errors():
    " run_cmd with errors"
    with pytest.raises(RuntimeError):
        run_cmd("false", error_mesg="ERROR command false failed")


def test_run_cmd_errors_no_check():
    " run_cmd with errors, but no check"
    run_cmd("false", check=False)
