" tests for the writer"
import os
import shutil

import pytest

from odbinfo.pure.writer import chdir, new_site
from odbinfo.test.resource import TEST_OUTPUT


def test_chdir_none():
    " test chdir on its default "
    cur_dir = os.getcwd()
    with chdir():
        os.chdir("/")
    assert os.getcwd() == cur_dir


@pytest.mark.slow
def test_new_site():
    """ test new site scaffolding """
    result = new_site(TEST_OUTPUT.format(""), "test-site")
    assert result == os.path.join(TEST_OUTPUT.format(""), "test-site")


@pytest.mark.slow
def test_new_site_exists():
    """ test new site scaffolding failure because exists """
    result = new_site(TEST_OUTPUT.format(""), "test-double")
    assert result == os.path.join(TEST_OUTPUT.format(""), "test-double")
    with pytest.raises(RuntimeError):
        new_site(TEST_OUTPUT.format(""), "test-double")


@pytest.mark.slow
def test_new_site_template_missing():
    """ test new site scaffolding failure because missing templates """
    shutil.move("data", "data.bak")
    with pytest.raises(RuntimeError):
        new_site(TEST_OUTPUT.format(""), "test-third")
    shutil.move("data.bak", "data")
