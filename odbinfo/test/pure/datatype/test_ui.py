" ui classes test "

import unittest

import odbinfo.test.pure.datatype.factory as factory
from odbinfo.pure.datatype.ui import Grid, TextDocument


class ReportTest(unittest.TestCase):

    def setUp(self):
        self.report = factory.report()

    def test_report_children(self):
        assert list(self.report.children()) == []

    def test_report_cmd(self):
        assert self.report.command == "plant"
        assert self.report.commandtype == "table"


def test_report_children_embedded():
    report_embeddedquery = factory.report_embeddedquery()
    embedded_query = factory.embedded_query()
    assert list(report_embeddedquery.children()) == [embedded_query]


class TextDocumentTest(unittest.TestCase):

    def setUp(self):
        self.textdoc = factory.textdoc()

    def test_text_document(self):
        assert self.textdoc.children() == []

    def test_text_document_user_match(self):
        assert self.textdoc.users_match("plant.odt")
        assert self.textdoc.users_match("plant")


def test_eventlistener():
    eventlistener = factory.eventlistener()
    assert eventlistener.parsescript() == "Library1.Module1.Main"


def test_control_children():
    control = factory.control()
    eventlistener = factory.eventlistener()
    assert list(control.children()) == [eventlistener]


class ListBoxText(unittest.TestCase):

    def setUp(self):
        self.listbox = factory.listbox()

    def test_listbox_command(self):
        assert self.listbox.command == 'SELECT * FROM "Plant"'
        assert self.listbox.commandtype == "rawsql"

    def test_listbox_children(self):
        assert self.listbox.children() == []


class ListBoxEmbeddedQueryText(ListBoxText):

    def setUp(self):
        super().setUp()
        self.embedded_query = factory.embedded_query()
        self.listbox.embedded_query = self.embedded_query

    def test_listbox_children(self):
        assert self.listbox.children() == [self.embedded_query]


def test_grid_children():
    grid = Grid("MyGrid", [], "Grid")

    assert grid.children() == []


def test_subform():
    subform = factory.subform()
    control = subform.controls[0]

    assert subform.children() == [control]


def test_subform_children_embedded():
    subform = factory.subform_embeddedquery()

    assert subform.children() == [subform.embedded_query]


def test_form_children():
    form = factory.form()

    assert form.children() == form.subforms
