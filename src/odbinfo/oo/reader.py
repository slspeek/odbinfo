""" Reads the metadata from a running LibreOffice and from the odb file.

    Note that tables, views and queries are read using a connection or
    datasource to LibreOffice.
    Forms, reports, libraries, pythonlibraries are
    read from the ODB-file as zip.
    Text-documents are searched for on config.textdocuments.search_locations,
    and are opened as zip.
"""
from pathlib import Path
from zipfile import ZipFile

from odbinfo.oo.ooutil import open_connection
from odbinfo.oo.tabular_reader import read_queries, read_tables, read_views
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.reader import (read_forms, read_libraries,
                                 read_python_libraries, read_reports,
                                 read_text_documents)
from odbinfo.pure.util import timed


@timed("Read metadata", indent=2)
def read_metadata(config: Configuration, datasource,
                  odbpath: Path) -> Metadata:
    """ reads all metadata """
    with open_connection(datasource) as con:
        with ZipFile(odbpath, "r") as odbzip:
            return \
                Metadata(name=config.name,
                         table_defs=read_tables(con),
                         view_defs=read_views(con),
                         query_defs=read_queries(con, datasource),
                         form_defs=read_forms(odbzip),
                         report_defs=read_reports(odbzip),
                         library_defs=read_libraries(odbzip),
                         pythonlibrary_defs=read_python_libraries(odbzip),
                         textdocument_defs=read_text_documents(config.textdocuments))
