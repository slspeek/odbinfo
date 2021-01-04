""" test site creation """
import os
from resource import TEST_OUTPUT
from odbinfo.writer import create_jekyll_site, _make_site
from odbinfo.reader import read_tables
from connect import datasource


def test_new_site():
    """ test new site scaffolding """
    result = create_jekyll_site(TEST_OUTPUT.format(""), "test-site")
    assert result == os.path.join(TEST_OUTPUT.format(""), "test-site")


def test_generate_tables_site():
    """ test table rendering """
    tables = read_tables(datasource().getConnection("", ""))
    _make_site(TEST_OUTPUT.format(""), "table-site", tables)
