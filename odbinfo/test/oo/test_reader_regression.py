""" Test the reader and create fixture(s) """
import pytest

from odbinfo.oo.reader import read_metadata
from odbinfo.test.oo.connect import libreoffice  # pylint:disable=unused-import
from odbinfo.test.oo.connect import datasource
from odbinfo.test.pure.fixtures import metadata  # pylint:disable=unused-import
from odbinfo.test.resource import DEFAULT_TESTDB


# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name
@pytest.mark.slow
def test_metadata_regression(libreoffice, metadata):
    """ make fixture """
    dsource = datasource()
    metadata_read = read_metadata(dsource, DEFAULT_TESTDB)
    assert metadata_read == metadata
