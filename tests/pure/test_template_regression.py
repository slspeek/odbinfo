""" writer regression tests """
import shutil
from pathlib import Path

import pytest

from odbinfo.pure.builder import run_gohugo
from tests.util import clear_generated_graphs


@pytest.mark.slow
def test_template_regression(fixture_path, directory_regression):
    """ Run without database scan """
    perform_template_regression_test("test_write_site", fixture_path,
                                     directory_regression)


@pytest.mark.slow
def test_template_regression_empty(fixture_path, directory_regression):
    """ Run without database scan """
    perform_template_regression_test("test_write_site_empty", fixture_path,
                                     directory_regression)


def perform_template_regression_test(name, fixture_path, directory_regression):
    """ run gohugo and verify"""

    site_path: Path = fixture_path / "template_regression_input" / name
    shutil.rmtree(site_path / "layouts")
    shutil.copytree("src/hugo-template/layouts", site_path / "layouts")
    run_gohugo(site_path)
    shutil.rmtree(site_path / "layouts")
    clear_generated_graphs(site_path)
    directory_regression.check(site_path)
