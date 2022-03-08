""" test reading odt and ott files """
import unittest
from pathlib import Path

import pytest

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.reader.textdoc import (
    _text_documents, create_database_display, create_text_document,
    database_displays, filter_displays, filtered_displays, read_text_documents)
from tests.resource import DEFAULT_TESTDB

from ..reader.test_common import OO_NAMESPACES, XMLTest

DISPLAY_ELEMENT = f"""
<text:database-display {OO_NAMESPACES} office:version="1.2" text:table-name="vwPlant" text:table-type="query" text:column-name="naam" text:database-name="testdb">&lt;naam&gt;</text:database-display>
"""


class Display(XMLTest):

    def setUp(self):
        self.xml = DISPLAY_ELEMENT
        self.db_display = create_database_display(self.root)

    def test_database_name(self):
        assert self.db_display.database == "testdb"

    def test_column_name(self):
        assert self.db_display.name == "naam"

    def test_table_name(self):
        assert self.db_display.table == "vwPlant"

    def test_table_type(self):
        assert self.db_display.tabletype == "query"


TEXT_DOC_ELEMENT = f"""<?xml version="1.0" encoding="UTF-8"?>
<office:document-content {OO_NAMESPACES} office:version="1.2">
  <office:scripts/>
  <office:font-face-decls>
    <style:font-face style:name="FreeSans1" svg:font-family="FreeSans" style:font-family-generic="swiss"/>
    <style:font-face style:name="Liberation Serif" svg:font-family="&apos;Liberation Serif&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
    <style:font-face style:name="Liberation Sans" svg:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="swiss" style:font-pitch="variable"/>
    <style:font-face style:name="DejaVu Sans" svg:font-family="&apos;DejaVu Sans&apos;" style:font-family-generic="system" style:font-pitch="variable"/>
    <style:font-face style:name="FreeSans" svg:font-family="FreeSans" style:font-family-generic="system" style:font-pitch="variable"/>
  </office:font-face-decls>
  <office:automatic-styles/>
  <office:body>
    <office:text>
      <text:sequence-decls>
        <text:sequence-decl text:display-outline-level="0" text:name="Illustration"/>
        <text:sequence-decl text:display-outline-level="0" text:name="Table"/>
        <text:sequence-decl text:display-outline-level="0" text:name="Text"/>
        <text:sequence-decl text:display-outline-level="0" text:name="Drawing"/>
        <text:sequence-decl text:display-outline-level="0" text:name="Figure"/>
      </text:sequence-decls>
      <text:p text:style-name="Standard">
        <text:database-display text:table-name="vwPlant" text:table-type="query" text:column-name="naam" text:database-name="testdb">&lt;naam&gt;</text:database-display>
      </text:p>
    </office:text>
  </office:body>
</office:document-content>

"""


class DatabaseDisplays(XMLTest):

    def setUp(self):
        self.xml = TEXT_DOC_ELEMENT
        self.db_displays = database_displays(self.root)

    def test_one_display(self):
        assert len(self.db_displays) == 1


class FilterDisplays(XMLTest):

    def setUp(self):
        self.xml = TEXT_DOC_ELEMENT
        self.db_displays = database_displays(self.root)
        self.config = TextDocumentsConfig(db_registration_id="testdb",
                                          search_locations=[])

    @property
    def filtered(self):
        return filter_displays(self.config, self.db_displays)

    def test_one_display(self):
        self.config = TextDocumentsConfig(db_registration_id="testdb",
                                          search_locations=[])
        assert len(self.filtered) == 1

    def test_no_display(self):
        self.config = TextDocumentsConfig(db_registration_id="nottestdb",
                                          search_locations=[])
        assert len(self.filtered) == 0


class FilteredDisplays(XMLTest):

    def setUp(self):
        self.xml = TEXT_DOC_ELEMENT
        self.config = TextDocumentsConfig(db_registration_id="testdb",
                                          search_locations=[])

    @property
    def filtered(self):
        return filtered_displays(self.config, self.root)

    def test_one_display(self):
        self.config = TextDocumentsConfig(db_registration_id="testdb",
                                          search_locations=[])
        assert len(self.filtered) == 1

    def test_no_display(self):
        self.config = TextDocumentsConfig(db_registration_id="nottestdb",
                                          search_locations=[])
        assert len(self.filtered) == 0


class TextDocument(unittest.TestCase):

    def setUp(self):
        self.doc_path = Path("/data/MyDocument.odt")
        self.textdoc = create_text_document(self.doc_path, [])

    def test_doc_name(self):
        assert self.textdoc.name == "MyDocument"

    def test_file_name(self):
        assert self.textdoc.filename == "MyDocument.odt"

    def test_path(self):
        assert self.textdoc.path == "/data/MyDocument.odt"


@pytest.mark.slow
def test_text_document(shared_datadir):
    """ find odts """
    directory = (shared_datadir / DEFAULT_TESTDB).parent
    assert len(list(_text_documents(directory))) == 3


@pytest.mark.slow
def test_read_text_documents(shared_datadir):
    """ find odts """
    directory = str((shared_datadir / DEFAULT_TESTDB).parent)
    assert len(
        read_text_documents(
            TextDocumentsConfig(db_registration_id="testdb",
                                search_locations=[directory]))) == 1
