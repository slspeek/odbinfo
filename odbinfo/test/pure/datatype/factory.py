" factory of test objects "
from odbinfo.pure.datatype.tabular import EmbeddedQuery
from odbinfo.pure.datatype.ui import (Control, EventListener, Form, Grid,
                                      ListBox, Report, SubForm, TextDocument)


def embedded_query():
    return EmbeddedQuery(
        "name", "select * from Plant")


def report():
    return Report("plants_report",
                  "plant",
                  "table",
                  "doc", [])


def report_embeddedquery():
    areport = Report("plants_report",
                     "select * from plant",
                     "command",
                     "doc", [])
    areport.embedded_query = embedded_query()
    return areport


def eventlistener():
    return EventListener("form:performaction",
                         "vnd.sun.star.script:Library1.Module1.Main?"
                         "language=Basic&location=document")


def control():
    return Control("ControlName",
                   "control1",
                   "datafield",
                   True,
                   True,
                   "label",
                   "formfor",
                   "type",
                   [eventlistener()])


def listbox():
    return ListBox("ControlName",
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
                   'SELECT * FROM "Plant"')


def subform_empty():
    return \
        SubForm("@form:name",
                "@form:command",
                "@form:command-type",
                "@form:allow-deletes",
                "@form:allow-updates",
                "@form:allow-inserts",
                "@form:master-fields",
                "@form:detail-fields",
                [],
                [])


def subform():
    asubform = subform_empty()
    asubform.controls = [control()]
    return asubform


def subform_embeddedquery():
    asubform = subform_empty()
    asubform.embedded_query = embedded_query()
    return asubform


def form():
    return Form("MyForm", [subform()])


def textdoc():
    return TextDocument("plant",
                        "plant.odt",
                        "template/plant.odt", [])
