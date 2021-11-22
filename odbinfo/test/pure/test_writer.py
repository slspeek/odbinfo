" tests for the writer"
import os
from datetime import datetime
from pathlib import Path

import pytest
from graphviz import Digraph

from odbinfo.pure.writer import (backup_old_site, localsite, new_site,
                                 present_contenttypes, write_graphs)
from odbinfo.test.pure.datatype import factory


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
def test_new_site(tmpdir):
    """ test new site scaffolding """
    site_path = Path(tmpdir) / "test-site"
    assert not site_path.exists()
    new_site(site_path)
    assert site_path.exists()
    assert (site_path / "static").exists()


def test_present_contenttypes():
    metadata = factory.metadata_listbox()
    assert present_contenttypes(metadata) == ['table', 'form']
