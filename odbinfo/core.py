""" Core module """
import os
from contextlib import contextmanager
from urllib.parse import urlparse
from odbinfo.writer import _make_site
from odbinfo.reader import read_tables


@contextmanager
def open_connection(datasource):
    """ contextmanager for libreoffice database connections """
    conn = datasource.getConnection("", "")
    try:
        yield conn
    finally:
        conn.close()
        conn.dispose()


def generate_report(oodocument):
    """ Make report """
    docurl = oodocument.URL
    docpath = urlparse(docurl).path
    workingdir = os.path.dirname(docpath)
    name, _ = os.path.splitext(os.path.basename(docpath))
    with open_connection(oodocument.DataSource) as con:
        tables = read_tables(con)
    _make_site(workingdir, name, tables)
