"reading odt and ott files"
from pathlib import Path
from typing import Generator, List
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype import DatabaseDisplay, TextDocument
from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.reader.common import document


def _text_documents(dir_path: Path) -> Generator[Path, None, None]:
    return dir_path.glob("**/*.o[dt]t")


def _database_displays(doc_path: Path) -> List[DatabaseDisplay]:
    def _unnumbered_database_displays(doc_path: Path) -> List[DatabaseDisplay]:
        def display(db_display_elem: Element):
            return \
                DatabaseDisplay(
                    db_display_elem.getAttribute("text:column-name"),
                    db_display_elem.getAttribute("text:database-name"),
                    db_display_elem.getAttribute("text:table-name"),
                    db_display_elem.getAttribute("text:table-type")
                )
        with ZipFile(doc_path) as file:
            body = document(file, "content.xml")\
                .getElementsByTagName("office:text")[0]
            return list(map(display, body.getElementsByTagName("text:database-display")))
    displays = _unnumbered_database_displays(doc_path)
    for index, display in zip(range(len(displays)), displays):
        display.index = index
    return displays


def read_text_documents(config: TextDocumentsConfig) -> List[TextDocument]:
    " search odt, ott files and look for database-display fields"
    docs = []
    if config.search_locations:
        for search_loc in config.search_locations:
            for doc_path in _text_documents(Path(search_loc)):
                displays = _database_displays(doc_path)
                displays = list(filter(
                    lambda d: d.database == config.db_registration_id,
                    displays
                ))
                if len(displays) > 0:
                    docs.append(
                        TextDocument(
                            doc_path.stem,
                            doc_path.name,
                            str(doc_path),
                            displays
                        )
                    )
    return docs
