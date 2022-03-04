""" LibreOffice specific utils """
import pathlib
import sys
import urllib
from contextlib import contextmanager


@contextmanager
def open_connection(datasource):
    """ contextmanager for libreoffice database connections """
    conn = datasource.getConnection("", "")
    try:
        yield conn
    finally:
        conn.close()
        conn.dispose()


def path_from_url(url: str) -> str:
    """ Extracts the filepath from the `url` """
    path = urllib.parse.urlparse(url).path

    if sys.platform.startswith("win"):
        path = path.lstrip("/")

    return urllib.parse.unquote(path)


def document_path(oodoc) -> pathlib.Path:
    """returns path object for `oodoc` which is a staroffice (local) document"""
    return pathlib.Path(path_from_url(oodoc.URL))
