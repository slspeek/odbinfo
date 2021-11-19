""" LibreOffice specific utils """
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlparse


@contextmanager
def open_connection(datasource):
    """ contextmanager for libreoffice database connections """
    conn = datasource.getConnection("", "")
    try:
        yield conn
    finally:
        conn.close()
        conn.dispose()


def document_path(oodoc) -> Path:
    "returns path object for `oodoc`"
    return Path(urlparse(oodoc.URL).path)
