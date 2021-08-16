"tests for metadata"
import pytest

from odbinfo.pure.datatype import Table
from odbinfo.pure.datatype.metadata import Metadata


def test_post_init():
    " test __post_init__ method"
    meta = Metadata([], [], [], [], [], [], [], [], [])
    assert meta


def test_verify_titles_unique():
    " test verify titles unique"
    meta = Metadata("testmeta", [Table("Plant", "", [], [], []), Table("Plant", "", [], [], [])],
                    [],  [], [], [], [], [], [])
    with pytest.raises(AssertionError):
        meta.verify_titles_unique_in_kind()
