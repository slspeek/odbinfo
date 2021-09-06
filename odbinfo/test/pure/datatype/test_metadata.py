"tests for metadata"
import pytest

from odbinfo.pure.datatype.metadata import Metadata


def test_post_init():
    " test __post_init__ method"
    meta = Metadata([], [], [], [], [], [], [], [], [])
    assert meta
