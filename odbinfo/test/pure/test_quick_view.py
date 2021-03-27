""" Quick view for the objects fixture """
import pytest

from odbinfo.pure.processor import process_metadata
from odbinfo.pure.writer import make_site
from odbinfo.test.pure.fixtures import metadata  # pylint:disable=unused-import
from odbinfo.test.resource import TEST_OUTPUT


# pylint:disable=redefined-outer-name
@pytest.mark.slow
def test_quick_view(metadata):
    """ Run without database scan """
    name = "testdb"
    outdir = TEST_OUTPUT.format("")
    make_site(outdir, name, metadata)


# pylint:disable=redefined-outer-name
def test_parse_libraries(metadata):
    """ parse libraries """
    process_metadata(metadata)
    print(metadata.libraries)
