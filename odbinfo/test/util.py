" Test utils"
import os
import shutil
from pathlib import Path

import pytest
from pytest import fixture


class DirectoryRegressionFixture:
    "Provides a directory regression test"

    def __init__(self, datadir, original_datadir, request):
        self.datadir = datadir
        self.original_datadir = original_datadir
        self.request = request

    def prepend_path(self, path) -> Path:
        "prepends `path` function name"
        return Path(path) / self.request.function.__name__

    @property
    def fixture_path(self):
        "reading fixture path"
        return self.prepend_path(Path(self.datadir))

    @property
    def fixture_original_path(self):
        "writing fixture path"
        return self.prepend_path(Path(self.original_datadir))

    def check(self, path_obtained: Path):
        """verifies that `path_obtained` is equal to an earlier
         version of `path_obtained`"""
        try:
            assert os.system(
                f"diff -r {str(self.fixture_path)}/ {str(path_obtained)}/") == 0
        except AssertionError as asexcep:
            if self.request.config.getoption("force_regen"):
                self.recreate_fixture(path_obtained)
                pytest.fail(f"recreated {self.fixture_original_path} fixture")
            else:
                raise asexcep

    def recreate_fixture(self, path_obtained: Path):
        "recreates this fixture with contents of `path_obtained`"
        if self.fixture_path.exists():
            shutil.rmtree(self.original_datadir)
        self.original_datadir.mkdir(exist_ok=True)
        shutil.copytree(path_obtained, self.original_datadir
                        / self.request.function.__name__)


@fixture(scope="function")
def directory_regression(datadir, original_datadir,  request):
    "directory_regression fixture"
    yield DirectoryRegressionFixture(datadir, original_datadir,
                                     request)


def remove_generated_graphs(path: Path):
    "clear generated graphs as they depend in dot version"
    for svgfile in path.glob("**/*.gv.svg"):
        svgfile.unlink()
