" ui classes test "

from odbinfo.pure.datatype.tabular import EmbeddedQuery
from odbinfo.pure.datatype.ui import (Control, EventListener, Form, Grid,
                                      ListBox, Report, SubForm, TextDocument)

REPORT = Report("plants_report",
                "plant",
                "table",
                "doc", [])

REPORT_EMBEDDEDQUERY = Report("plants_report",
                              "plant",
                              "table",
                              "doc", [])
EMBEDDED_QUERY = EmbeddedQuery(
    "name", "select * from Plant")
REPORT_EMBEDDEDQUERY.embedded_query = EMBEDDED_QUERY


def test_report_children() -> None:
    assert list(REPORT.children()) == []


def test_report_children_embedded() -> None:
    assert list(REPORT_EMBEDDEDQUERY.children()) == [EMBEDDED_QUERY]


def test_report_cmd():
    assert REPORT.command == "plant"
    assert REPORT.commandtype == "table"


TEXTDOC = TextDocument("plant", "plant.odt", "template/plant.odt", [])


def test_text_document():
    assert TEXTDOC.children() == []


def test_text_document_user_match():
    assert TEXTDOC.users_match("plant.odt")
    assert TEXTDOC.users_match("plant")


EVENTLISTENER = EventListener("form:performaction",
                              "vnd.sun.star.script:Library1.Module1.Main?"
                              "language=Basic&location=document")


def test_eventlistener():
    assert EVENTLISTENER.parsescript() == "Library1.Module1.Main"


CONTROL = Control("ControlName",
                  "control1",
                  "datafield",
                  True,
                  True,
                  "label",
                  "formfor",
                  "type",
                  [EVENTLISTENER])


def test_control_children():
    assert list(CONTROL.children()) == [EVENTLISTENER]


LISTBOX = ListBox("ControlName",
                  "control1",
                  "datafield",
                  True,
                  True,
                  "label",
                  "formfor",
                  "type",
                  [],
                  1,
                  True,
                  "rawsql",
                  "SELECT")


def test_listbox():
    assert LISTBOX.command == "SELECT"
    assert LISTBOX.commandtype == "rawsql"
    assert LISTBOX.children() == []


LISTBOX_EMDEDDEDQUERY = ListBox("ControlName",
                                "control1",
                                "datafield",
                                True,
                                True,
                                "label",
                                "formfor",
                                "type",
                                [],
                                1,
                                True,
                                "rawsql",
                                "SELECT")

LISTBOX_EMDEDDEDQUERY.embedded_query = EMBEDDED_QUERY


def test_listbox_embeddedquery():
    assert LISTBOX_EMDEDDEDQUERY.children() == [EMBEDDED_QUERY]


GRID = Grid("MyGrid", [], "Grid")


def test_grid_children():
    assert GRID.children() == []


SUBFORM = SubForm("@form:name",
                  "@form:command",
                  "@form:command-type",
                  "@form:allow-deletes",
                  "@form:allow-updates",
                  "@form:allow-inserts",
                  "@form:master-fields",
                  "@form:detail-fields",
                  [CONTROL],
                  [])


def test_subform():
    assert SUBFORM.children() == [CONTROL]


SUBFORM_EMBEDDEQUERY = SubForm("@form:name",
                               "@form:command",
                               "@form:command-type",
                               "@form:allow-deletes",
                               "@form:allow-updates",
                               "@form:allow-inserts",
                               "@form:master-fields",
                               "@form:detail-fields",
                               [],
                               [])
SUBFORM_EMBEDDEQUERY.embedded_query = EMBEDDED_QUERY


def test_subform_children_embedded():
    assert SUBFORM_EMBEDDEQUERY.children() == [EMBEDDED_QUERY]


FORM = Form("MyForm", [SUBFORM])


def test_form_children():
    assert FORM.children() == [SUBFORM]
