""" Test the reader and create fixture(s) """
import pytest

from odbinfo.oo.reader import read_metadata
from odbinfo.test.oo.connect import datasource, empty_libreoffice, libreoffice
from odbinfo.test.pure.fixtures import empty_metadata, metadata
from odbinfo.test.resource import DEFAULT_TESTDB, EMPTYDB


def read_metadata_in_test(dbpath):
    "read_metadata in test setting"
    dsource = datasource()
    return read_metadata(dsource, dbpath)


def read_metadata_regression_test(dbpath, metadata_fixture):
    " runs read_metadata and asserts nothing changed "
    metadata_read = read_metadata_in_test(dbpath)
    assert metadata_read == metadata_fixture


@pytest.mark.slow
def test_metadata_regression(libreoffice, metadata):
    """ test read_metadata for regression """
    read_metadata_regression_test(DEFAULT_TESTDB, metadata)


@pytest.mark.slow
def test_metadata_regression_empty(empty_libreoffice, empty_metadata):
    """ test read_metadata for regression """
    read_metadata_regression_test(EMPTYDB, empty_metadata)
