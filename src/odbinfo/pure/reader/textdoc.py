"""reading odt and ott files"""
from pathlib import Path
from typing import Generator, List
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.datatype.ui import DatabaseDisplay, TextDocument
from odbinfo.pure.reader.common import CONTENT_XML, document_element
from odbinfo.pure.util import timed


def find_text_documents(dir_path: Path) -> Generator[Path, None, None]:
    """ Returns generator for staroffice text documents and templates
        in the directory `dir_path' and its subdirectories.
    """
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


def filtered_displays(db_registration_id: str,
                      doc_element: Element) -> List[DatabaseDisplay]:
    """ returns the database-displays that match `db_registration_id` from the `doc_elem`"""
    return [
        display for display in database_displays(doc_element)
        if display.database == db_registration_id
    ]


def create_text_document(doc_path: Path,
                         displays: List[DatabaseDisplay]) -> TextDocument:
    """ returns a TextDocument from `doc_path` and `displays`"""
    return TextDocument(doc_path.stem, doc_path.name, str(doc_path), displays)


@timed("Reading text documents", indent=4)
def read_text_documents(config: TextDocumentsConfig) -> List[TextDocument]:
    """ Search for staroffice text document and text template files and looks
        for database-display fields that match our db_registration_id.
        Returns a list of TextDocuments found in the specified locations that match.
    """
    docs: List[TextDocument] = []
    if not config.search_locations:
        return docs

    for search_loc in config.search_locations:
        for doc_path in find_text_documents(Path(search_loc)):
            with ZipFile(doc_path) as doc_zip:
                doc_element: Element = document_element(doc_zip, CONTENT_XML)
                displays: List[DatabaseDisplay] = filtered_displays(
                    config.db_registration_id, doc_element)
                if len(displays) > 0:
                    docs.append(create_text_document(doc_path, displays))
    return docs
