""" LibreOffice specific utils """
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
