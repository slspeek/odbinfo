" test the xml reading utility functions "
import unittest

import pytest

from odbinfo.pure.reader.common import (_collect_attribute, child_elements,
                                        document, document_element)
from odbinfo.test.pure.fixtures import odbzip


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
