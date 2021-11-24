""" test dependency search in ui """
import unittest

from odbinfo.pure.datatype.base import WebPage
from odbinfo.pure.datatype.exec import BasicFunction
from odbinfo.pure.datatype.ui import DatabaseDisplay
from odbinfo.pure.dependency.searchui import (
    search_basicfunction_in_eventlistener, search_deps_in_commander,
    search_deps_in_documents)
from odbinfo.test.pure.datatype import factory


class InCommanderTest(unittest.TestCase):
    """search_deps_in_commander"""

    def setUp(self):
        self.webpage = WebPage("plant")
        self.report = factory.report()

    def test_search_deps_in_commander(self):
        """match"""
        search_deps_in_commander([self.webpage], [self.report])
        self.assertTrue(self.report.link == self.webpage.identifier)

    def test_search_deps_in_commander_embedded(self):
        """no match"""
        search_deps_in_commander(
            [self.webpage], [factory.report_embeddedquery()])
        self.assertIsNone(self.report.link)


class DepsInDocumentsTest(unittest.TestCase):
    """search_deps_in_documents"""

    def setUp(self):
        self.textdoc = factory.textdoc()
        self.display = DatabaseDisplay("id", "testdb", "plant", "table")
        self.textdoc.fields.append(self.display)
        self.table_plant = WebPage("plant")

    def test_search_deps_in_document(self):
        """match"""
        search_deps_in_documents([self.table_plant], [self.textdoc])
        self.assertTrue(self.display.link == self.table_plant.identifier)

    def test_search_deps_in_document_no_match(self):
        """no match"""
        search_deps_in_documents([WebPage("not_plant")], [self.textdoc])
        self.assertIsNone(self.display.link)


class DepsInEventListenerTest(unittest.TestCase):
    """search_basicfunction_in_eventlistener"""

    def setUp(self):
        self.func = BasicFunction("Main", "Library1", "Module1")
        self.eventlistener = factory.eventlistener()

    def test_search_basicfunction_in_eventlistener(self):
        """match"""
        search_basicfunction_in_eventlistener(
            [self.func], [self.eventlistener])
        self.assertTrue(self.eventlistener.link == self.func.identifier)

    def test_search_basicfunction_in_eventlistener_no_match(self):
        """no match"""
        search_basicfunction_in_eventlistener(
            [BasicFunction("NotMain", "Library1", "Module1")], [self.eventlistener])
        self.assertIsNone(self.eventlistener.link)
