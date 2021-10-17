" test reading odt and ott files "
import unittest
from pathlib import Path

import pytest

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.reader.textdoc import (_text_documents, database_displays,
                                         display, filter_displays,
                                         filtered_displays,
                                         read_text_documents, text_document)
from odbinfo.test.pure.reader.test_common import XMLTest
from odbinfo.test.resource import DEFAULT_TESTDB

DISPLAY_ELEMENT = """
<text:database-display xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ooo="http://openoffice.org/2004/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" office:version="1.2" text:table-name="vwPlant" text:table-type="query" text:column-name="naam" text:database-name="testdb">&lt;naam&gt;</text:database-display>
"""


class Display(XMLTest):

    def setUp(self):
        self.xml = DISPLAY_ELEMENT
        self.db_display = display(self.root)

    def test_database_name(self):
        assert self.db_display.database == "testdb"

    def test_column_name(self):
        assert self.db_display.name == "naam"

    def test_table_name(self):
        assert self.db_display.table == "vwPlant"

    def test_table_type(self):
        assert self.db_display.tabletype == "query"


TEXT_DOC_ELEMENT = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ooo="http://openoffice.org/2004/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" office:version="1.2">
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
        self.config = TextDocumentsConfig("testdb", [])

    @property
    def filtered(self):
        return filter_displays(self.config, self.db_displays)

    def test_one_display(self):
        self.config = TextDocumentsConfig("testdb", [])
        assert len(self.filtered) == 1

    def test_no_display(self):
        self.config = TextDocumentsConfig("nottestdb", [])
        assert len(self.filtered) == 0


class FilteredDisplays(XMLTest):

    def setUp(self):
        self.xml = TEXT_DOC_ELEMENT
        self.config = TextDocumentsConfig("testdb", [])

    @property
    def filtered(self):
        return filtered_displays(self.config, self.root)

    def test_one_display(self):
        self.config = TextDocumentsConfig("testdb", [])
        assert len(self.filtered) == 1

    def test_no_display(self):
        self.config = TextDocumentsConfig("nottestdb", [])
        assert len(self.filtered) == 0


class TextDocument(unittest.TestCase):

    def setUp(self):
        self.doc_path = Path("/data/MyDocument.odt")
        self.textdoc = text_document(self.doc_path, [])

    def test_doc_name(self):
        assert self.textdoc.name == "MyDocument"

    def test_file_name(self):
        assert self.textdoc.filename == "MyDocument.odt"

    def test_path(self):
        assert self.textdoc.path == "/data/MyDocument.odt"


@pytest.mark.slow
def test_text_document(shared_datadir):
    " find odts "
    directory = (shared_datadir / DEFAULT_TESTDB).parent
    assert len(list(_text_documents(directory))) == 3


@pytest.mark.slow
def test_read_text_documents(shared_datadir):
    " find odts "
    directory = (shared_datadir / DEFAULT_TESTDB).parent
    assert len(read_text_documents(TextDocumentsConfig("testdb", [directory])))
