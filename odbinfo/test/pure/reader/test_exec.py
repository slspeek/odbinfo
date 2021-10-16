" test reding of libraries "
import pytest

from odbinfo.pure.reader.exec import read_libraries, read_python_libraries
from odbinfo.test.pure.fixtures import empty_odbzip, odbzip


@pytest.mark.slow
def test_libraries_empty(empty_odbzip):
    " no libraries  "
    read_libraries(empty_odbzip)


@pytest.mark.slow
def test_libraries(odbzip):
    " libraries "
    read_libraries(odbzip)


@pytest.mark.slow
def test_pylibraries(odbzip):
    " libraries "
    libs = read_python_libraries(odbzip)
    # print(libs)
    assert len(libs) == 2
    assert len(libs[0].modules) == 1
    assert len(libs[1].modules) == 1
