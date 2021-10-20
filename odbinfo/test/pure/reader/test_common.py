" test the xml reading utility functions "
import unittest

import pytest

from odbinfo.pure.reader.common import (_collect_attribute, child_elements,
                                        document, document_element)
from odbinfo.test.pure.fixtures import odbzip

# pylint:disable=line-too-long
OO_NAMESPACES = """xmlns:db="urn:oasis:names:tc:opendocument:xmlns:database:1.0" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ooo="http://openoffice.org/2004/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" """


class ZipFileMock():  # pylint:disable=too-few-public-methods

    def read(self, path):
        pass


class XMLTest(unittest.TestCase):

    def setUp(self):
        self.xml = "<tag><foo></foo><bar/></tag>"

    @property
    def root(self):
        return document_element(self.xml)


class ChildElements(XMLTest):

    def setUp(self):
        self.xml = "<tag><foo></foo><bar/></tag>"

    def test_two_elem(self):
        assert len(child_elements(self.root)) == 2

    def test_empty(self):
        self.xml = "<tag></tag>"
        assert len(child_elements(self.root)) == 0


@pytest.mark.slow
def test_document(odbzip):
    doc = document(odbzip, "content.xml")
    # print(doc.toprettyxml())
    assert doc.tagName == "office:document-content"


def test_collect_attribute():
    " simple test "
    data = {"elem": {"@foo": "bar"}, "@foo": "foo"}
    assert _collect_attribute(data, "@foo") == ["bar", "foo"]


def test_collect_attribute1():
    " simple test "
    data = {"@foo": "bar"}
    assert _collect_attribute(data, "@foo") == ["bar"]


def test_collect_element():
    " simple test "
    data = {"@foo": "bar", "foo": {}}
    assert _collect_attribute(data, "foo") == [{}]
