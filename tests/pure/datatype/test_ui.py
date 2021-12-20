""" ui classes test """

from odbinfo.pure.datatype.ui import Grid


def test_report_children(report):
    assert not list(report.children())


def test_report_cmd(report):
    assert report.command == "plant"
    assert report.commandtype == "table"


def test_report_children_embedded(report_embeddedquery, embedded_query):
    assert list(report_embeddedquery.children()) == [embedded_query]


def test_text_document(textdoc):
    assert textdoc.children() == textdoc.fields


def test_text_document_user_match(textdoc):
    assert textdoc.users_match("plant.odt")
    assert textdoc.users_match("plant")


def test_eventlistener(eventlistener):
    assert eventlistener.parsescript() == "Library1.Module1.Main"


def test_control_children(control, eventlistener):
    assert list(control.children()) == [eventlistener]


def test_listbox_command(listbox):
    assert listbox.command == 'SELECT * FROM "Plant"'
    assert listbox.commandtype == "rawsql"


def test_listbox_children(listbox):
    assert listbox.children() == []


def test_listbox_children_embedded_query(listbox_embeddedquery):
    assert listbox_embeddedquery.children(
    ) == [listbox_embeddedquery.embedded_query]


def test_grid_children():
    grid = Grid("MyGrid", [], "Grid")
    assert not grid.children()


def test_subform(subform):
    control = subform.controls[0]
    assert subform.children() == [control]


def test_subform_children_embedded(subform_embeddedquery):
    assert subform_embeddedquery.children(
    ) == [subform_embeddedquery.embedded_query]


def test_form_children(form):
    assert form.children() == form.subforms
