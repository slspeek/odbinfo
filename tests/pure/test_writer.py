""" tests for the writer"""
import builtins
import datetime
import os
from io import StringIO
from pathlib import Path
from unittest import mock

import graphviz
import pytest

from odbinfo.pure import writer
from odbinfo.pure.datatype import metadata


def test_localsite_name():
    assert writer.localsite(Path("foo/bar")) == Path("foo/bar-local")


def test_localsite_short_path():
    assert writer.localsite(Path("bar")) == Path("bar-local")


def test_backup_old_site(tmpdir):
    """ test cleaning old site """
    os.makedirs(tmpdir / "exampledb")
    os.makedirs(tmpdir / "exampledb-local")
    writer.backup_old_site(Path(tmpdir) / "exampledb",
                           date=datetime.datetime(2010, 10, 10, 00, 00, 0))
    assert not (tmpdir / "exampledb").exists()
    assert not (tmpdir / "exampledb-local").exists()
    assert (tmpdir / "exampledb.bak.2010-10-10--00-00-00-000000").exists()


@pytest.mark.slow
def test_write_graphs(tmpdir):
    """test write graphs"""
    writer.write_graph(graphviz.Digraph("foo"), tmpdir)
    assert (tmpdir / "static" / "svg" / "foo.gv.svg").exists()
    assert (tmpdir / "static" / "svg" / "foo.gv").exists()


@pytest.mark.slow
def test_new_site(tmpdir):
    """ test new site scaffolding """
    site_path = Path(tmpdir) / "test-site"
    assert not site_path.exists()
    writer.new_site(site_path)
    assert site_path.exists()
    assert (site_path / "static").exists()


def test_present_contenttypes(metadata_listbox):
    assert writer.present_contenttypes(metadata_listbox) == [
        metadata.TopLevelDisplayedContent.TABLE,
        metadata.TopLevelDisplayedContent.FORM
    ]


def test_create_config(configuration):
    present_content = [metadata.TopLevelDisplayedContent.TABLE]
    assert writer.create_config(configuration, present_content) == {
        'baseURL': 'http://odbinfo.org/',
        'languageCode': 'en-us',
        'menu': {
            'main': [
                {
                    'name': 'home',
                    'url': '/',
                    'weight': 1
                },
                {
                    'name': 'diagram',
                    'url': '/svg/test_config.gv.svg',
                    'weight': 2
                },
                {
                    'name': 'table',
                    'url': '/table/index.html',
                    'weight': 3
                },
            ]
        },
        'theme': 'minimal',
        'title': 'test_config',
    }


def test_write_config():
    out_stream = StringIO()
    with mock.patch.object(builtins, "open",
                           return_value=out_stream) as open_mock:
        conf = {"foo": "42"}
        writer.write_config(Path("output_dir"), conf)
    open_mock.assert_called_with(Path("output_dir/config.toml"),
                                 "w",
                                 encoding="utf-8")


def test_frontmatter():
    out = StringIO()
    writer.frontmatter({"foo": "42"}, out)
    assert out.getvalue() == """---\nfoo: '42'\n---\n"""


def test_content_dir():
    assert writer.content_dir(
        Path("site"),
        metadata.TopLevelDisplayedContent.TABLE) == Path("site/content/table")
