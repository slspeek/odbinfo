"""reading odt and ott files"""
from pathlib import Path
from typing import Generator, List, Sequence
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.datatype.ui import DatabaseDisplay, TextDocument
from odbinfo.pure.reader.common import document_element
from odbinfo.pure.util import timed


def _text_documents(dir_path: Path) -> Generator[Path, None, None]:
    return dir_path.glob("**/*.o[dt]t")


def create_database_display(db_display_elem: Element):
    """ returns a DatabaseDisplay populated with the attributres of `db_display_elem`"""
    return \
        DatabaseDisplay(
            db_display_elem.getAttribute("text:column-name"),
            db_display_elem.getAttribute("text:database-name"),
            db_display_elem.getAttribute("text:table-name"),
            db_display_elem.getAttribute("text:table-type")
        )


def database_displays(doc_elem: Element) -> List[DatabaseDisplay]:
    """ returns a list of DatabaseDisplays created from the
        "text:database-display" elements under `doc_elem`
     """
    return [
        create_database_display(display_elem) for display_elem in
        doc_elem.getElementsByTagName("text:database-display")
    ]


def filter_displays(
        config: TextDocumentsConfig,
        displays: Sequence[DatabaseDisplay]) -> List[DatabaseDisplay]:
    """ filter by `config`.db_registration_id"""
    return \
        [display for display in displays if display.database
            == config.db_registration_id]


def filtered_displays(config: TextDocumentsConfig,
                      doc_element: Element) -> List[DatabaseDisplay]:
    """ filters the `doc_elem` database-diplays by `config`.db_registration_id"""
    return filter_displays(config, database_displays(doc_element))


def create_text_document(doc_path: Path,
                         displays: List[DatabaseDisplay]) -> TextDocument:
    """ returns a TextDocument from `doc_path` and `displays`"""
    return TextDocument(doc_path.stem, doc_path.name, str(doc_path), displays)


@timed("Reading text documents", indent=4)
def read_text_documents(config: TextDocumentsConfig) -> List[TextDocument]:
    """ search odt, ott files and look for database-display fields"""
    docs = []
    if config.search_locations:
        for search_loc in config.search_locations:
            for doc_path in _text_documents(Path(search_loc)):
                with ZipFile(doc_path) as doc_zip:
                    doc_element = document_element(doc_zip, "content.xml")
                    displays = filtered_displays(config, doc_element)
                    if len(displays) > 0:
                        docs.append(create_text_document(doc_path, displays))
    return docs
