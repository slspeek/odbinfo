" tests for the writer"
import os
import webbrowser
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import pytest
from graphviz import Digraph

from odbinfo.pure.writer import (CommandExecutionError, _is_port_open,
                                 backup_old_site, chdir, find_free_port,
                                 localsite, new_site, open_browser,
                                 present_contenttypes, run_cmd, write_graphs)
from odbinfo.test.pure.datatype import factory
from odbinfo.test.resource import TEST_OUTPUT_PATH


def test_find_free_port():
    free_port = find_free_port()
    assert not _is_port_open(free_port)


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


def test_localsite_name():
    assert localsite(Path("foo/bar")) == Path("foo/bar-local")


def test_localsite_short_path():
    assert localsite(Path("bar")) == Path("bar-local")


def test_backup_old_site(tmpdir):
    " test cleaning old site "
    os.makedirs(tmpdir / "exampledb")
    os.makedirs(tmpdir / "exampledb-local")
    backup_old_site(Path(tmpdir) / "exampledb",
                    date=datetime(2010, 10, 10, 00, 00, 0))
    assert not (tmpdir / "exampledb").exists()
    assert not (tmpdir / "exampledb-local").exists()
    assert (tmpdir / "exampledb.bak.2010-10-10--00-00-00-000000").exists()


@pytest.mark.slow
def test_write_graphs(tmpdir):
    "test write graphs"
    write_graphs([Digraph("foo")], tmpdir)
    assert (tmpdir / "static" / "svg" / "foo.gv.svg").exists()
    assert (tmpdir / "static" / "svg" / "foo.gv").exists()


@pytest.mark.slow
def test_new_site():
    """ test new site scaffolding """
    site_path = TEST_OUTPUT_PATH / "test-site"
    assert not site_path.exists()
    new_site(site_path)
    assert site_path.exists()
    assert (site_path / "static").exists()


def test_open_browser():
    " test the open_browser function "
    with patch.object(webbrowser, 'open') as openmock:
        with patch.object(os, 'getcwd', return_value="/home"):
            with patch.object(os, 'getenv', return_value="0"):
                open_browser(Path("site"))
    openmock.assert_called_with("file:///home/site/index.html")


def test_open_browser_absolutepath():
    " test the open_browser function "
    with patch.object(webbrowser, 'open') as openmock:
        with patch.object(os, 'getcwd', return_value="/home"):
            with patch.object(os, 'getenv', return_value="0"):
                open_browser(Path("/site"))
    openmock.assert_called_with("file:///site/index.html")


def test_open_browser_nop():
    " test the open_browser function doing nothing"
    with patch.object(webbrowser, 'open') as openmock:
        with patch.object(os, 'getcwd', return_value="/home"):
            with patch.object(os, 'getenv', return_value="1"):
                open_browser(Path("site"))
    openmock.assert_not_called()


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


def test_present_contenttypes():
    metadata = factory.metadata_listbox()
    assert present_contenttypes(metadata) == ['table', 'form']
