" tests for the writer"
import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from graphviz import Digraph

from odbinfo.pure.writer import (_open_browser, _write_graphs, chdir,
                                 clean_old_site, new_site, run_checked)
from odbinfo.test.resource import TEST_OUTPUT_TPL


def test_chdir_none():
    " test chdir on its default "
    cur_dir = os.getcwd()
    with chdir():
        os.chdir("/")
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
    open_browser = MagicMock()
    _open_browser("site", "/home", env_info="0", open_browser=open_browser)
    open_browser.assert_called_with("file:///home/site/index.html")


def test_open_browser_nop():
    " test the _open_browser function doing nothing"
    open_browser = MagicMock()
    _open_browser("site", "/home", env_info="1", open_browser=open_browser)
    open_browser.assert_not_called()


def test_run_checked():
    " run_checked without errors"
    run_checked("ls", "ERROR command ls failed")


def test_run_checked_errors():
    " run_checked with errors"
    with pytest.raises(RuntimeError):
        run_checked("false", "ERROR command false failed")
