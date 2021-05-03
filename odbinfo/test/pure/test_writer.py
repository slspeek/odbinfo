" tests for the writer"
import os
from unittest.mock import MagicMock

import pytest

from odbinfo.pure.writer import _open_browser, chdir, new_site, run_checked
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


def test_open_browser():
    " test the _open_browser function "
    # pylint:disable=missing-class-docstring
    class Browser:
        # pylint:disable=missing-function-docstring
        # pylint:disable=too-few-public-methods
        def open(self, uri):
            pass
    browser = Browser()
    browser.open = MagicMock()

    cwd = "/home"
    site_dir = "site"
    _open_browser(browser, cwd, site_dir)

    browser.open.assert_called_with("file:///home/site/index.html")


def test_run_checked():
    " run_checked without errors"
    run_checked("ls", "ERROR command ls failed")


def test_run_checked_errors():
    " run_checked with errors"
    with pytest.raises(RuntimeError):
        run_checked("false", "ERROR command false failed")
