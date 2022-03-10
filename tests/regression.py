"""  Directory regression fixture """
import os
import shutil
from pathlib import Path
from typing import List

import pytest
from pytest import fixture

GITKEEP = ".gitkeep"


def is_empty_dir(path: Path) -> bool:
    """Returns True if `path` is an empty directory"""
    return path.is_dir() and not list(path.glob("**/*"))


def find_empty_dirs(path: Path) -> List[Path]:
    """Recursively search `path` for empty directories"""
    if is_empty_dir(path):
        return [path]
    return [_dir for _dir in path.glob("**/*") if is_empty_dir(_dir)]


def create_gitkeep_in_empty_dirs(path):
    """ Creates an empty .gitkeep file in the empty directories under `path`"""
    for empty_dir in find_empty_dirs(path):
        with open(empty_dir / GITKEEP, 'w', encoding="UTF-8"):
            pass


class DirectoryRegressionFixture:
    """Provides a directory regression test"""

    def __init__(self, datadir, original_datadir, request):
        self.datadir = datadir
        self.original_datadir = original_datadir
        self.request = request

    def append_test_function_name(self, path) -> Path:
        """prepends `path` to the function name"""
        return Path(path) / self.request.function.__name__

    @property
    def fixture_path(self):
        """reading fixture path"""
        return self.append_test_function_name(Path(self.datadir))

    @property
    def fixture_original_path(self):
        """writing fixture path"""
        return self.append_test_function_name(Path(self.original_datadir))

    def check(self, path_obtained: Path):
        """verifies that `path_obtained` is equal to an earlier
         version of `path_obtained`"""
        create_gitkeep_in_empty_dirs(path_obtained)
        try:
            assert os.system(
                f"""diff -r "{str(self.fixture_path)}/" "{str(path_obtained)}/" """
            ) == 0
        except AssertionError as asexcep:
            if self.request.config.getoption("force_regen"):
                self.recreate_fixture(path_obtained)
                pytest.fail(f"recreated {self.fixture_original_path} fixture")
            else:
                raise asexcep

    def recreate_fixture(self, path_obtained: Path):
        """recreates this fixture with contents of `path_obtained`"""
        if self.fixture_path.exists():
            shutil.rmtree(self.original_datadir)
        self.original_datadir.mkdir(exist_ok=True)
        shutil.copytree(path_obtained, self.fixture_original_path)


@fixture(scope="function")
def directory_regression(datadir, original_datadir, request):
    """directory_regression fixture"""
    yield DirectoryRegressionFixture(datadir, original_datadir, request)
