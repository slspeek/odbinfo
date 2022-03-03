""" tests for the regression module """
import pathlib

import regression


def test_find_empty_dir(tmpdir):
    assert regression.find_empty_dirs(
        pathlib.Path(tmpdir)) == [pathlib.Path(tmpdir)]


def test_find_empty_subdir(tmpdir):
    empty_subdir = "empty_subdir"
    empty_path = pathlib.Path(tmpdir / empty_subdir)
    empty_path.mkdir()

    assert regression.find_empty_dirs(pathlib.Path(tmpdir)) == [empty_path]
