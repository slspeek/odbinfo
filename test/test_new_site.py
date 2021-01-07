""" test site creation """
import os
import logging
from test.connect import datasource, start_office
from test.resource import TEST_OUTPUT, DEFAULT_TESTDB
from pytest import fixture
import pytest
from odbinfo.writer import new_jekyll_site, _make_site
from odbinfo.reader import read_tables

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.DEBUG)


@pytest.mark.slow
# pylint:disable=unused-argument
def test_new_site(libreoffice):  # pylint:disable=redefined-outer-name
    """ test new site scaffolding """
    result = new_jekyll_site(TEST_OUTPUT.format(""), "test-site")
    assert result == os.path.join(TEST_OUTPUT.format(""), "test-site")


@fixture(scope="module")
def libreoffice():
    """ A libreoffice running on a test repository """
    testdb = os.getenv("BD_TESTDB", DEFAULT_TESTDB)
    office_proc = start_office(testdb)
    yield office_proc
    office_proc.terminate()
    logger.debug("LibreOffice killed")


@pytest.mark.slow
def test_generate_tables_site():
    """ test table rendering """
    tables = read_tables(datasource().getConnection("", ""))
    _make_site(TEST_OUTPUT.format(""), "table-site", tables)
