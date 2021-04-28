""" Quick view for the objects fixture """
import pytest

from odbinfo.pure.writer import make_site
from odbinfo.test.pure.fixtures import (  # pylint:disable=unused-import
    metadata, metadata_processed)
from odbinfo.test.resource import TEST_OUTPUT


# pylint:disable=redefined-outer-name
@pytest.mark.slow
def test_quick_view(metadata_processed):
    """ Run without database scan """
    name = "testdb"
    outdir = TEST_OUTPUT.format("")
    make_site(outdir, name, metadata_processed)
