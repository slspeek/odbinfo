""" Quick view for the objects fixture """
import pytest

from odbinfo.pure.writer import make_site
from odbinfo.test.pure.fixtures import (  # pylint:disable=unused-import
    empty_metadata_processed, metadata_processed)
from odbinfo.test.resource import TEST_OUTPUT


# pylint:disable=redefined-outer-name
@pytest.mark.slow
def test_quick_view(metadata_processed):
    """ Run without database scan """
    name = "testdb"
    outdir = TEST_OUTPUT.format("")
    make_site(outdir, name, metadata_processed)


# pylint:disable=redefined-outer-name
@pytest.mark.slow
def test_quick_view_empty(empty_metadata_processed):
    """ Run without database scan """
    name = "emptydb"
    outdir = TEST_OUTPUT.format("")
    make_site(outdir, name, empty_metadata_processed)
