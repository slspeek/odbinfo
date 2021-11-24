"""directory_regression test"""
from unittest.mock import patch

import pytest

from odbinfo.pure import builder
from odbinfo.pure.builder import convert_local
from odbinfo.test.pure.fixtures import fixture_path
from odbinfo.test.regression import directory_regression


@pytest.mark.slow
def test_convert_local_regression(directory_regression, fixture_path):
    with patch.object(builder, 'find_free_port', return_value=1313):
        convert_local(fixture_path / "convert_local_input")
        directory_regression.check(
            fixture_path / "convert_local_input-local",
        )
