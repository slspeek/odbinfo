""" tests for the builder module """
import os
import webbrowser
from pathlib import Path
from unittest.mock import patch

from odbinfo.pure.builder import find_free_port, is_port_open, open_browser


def test_find_free_port():
    free_port = find_free_port()
    assert not is_port_open(free_port)


def test_open_browser():
    """ test the open_browser function """
    with patch.object(webbrowser, 'open') as openmock:
        with patch.object(os, 'getcwd', return_value="/home"):
            open_browser(Path("site"))
    openmock.assert_called_with("file:///home/site/index.html")


def test_open_browser_absolutepath():
    """ test the open_browser function """
    with patch.object(webbrowser, 'open') as openmock:
        open_browser(Path("/site"))
    openmock.assert_called_with("file:///site/index.html")
