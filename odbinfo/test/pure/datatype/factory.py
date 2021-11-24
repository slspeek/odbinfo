""" factory of test objects """
from odbinfo.pure.datatype import Metadata
from odbinfo.pure.datatype.tabular import EmbeddedQuery, Key, Table
from odbinfo.pure.datatype.ui import (Control, EventListener, Form, Grid,
                                      ListBox, Report, SubForm, TextDocument)


def foreignkey_famliy():
    return Key("myFK", [], [], "family", 3, 1, 1)


def table_plant():
    foreign = foreignkey_famliy()
    plant = Table("plant", "", [foreign], [], [])
    foreign.parent = plant
    return plant


def table_family():
    return Table("family", "", [], [], [])


def embedded_query():
    return EmbeddedQuery(
        "myEmbeddedQuery", "select * from Plant")


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


def irrelevant_control():
    return Control("ControlName",
                   "control1",
                   "datafield",
                   True,
                   True,
                   "label",
                   "formfor",
                   "type",
                   [])


def control():
    acontrol = irrelevant_control()
    acontrol.eventlisteners.append(eventlistener())
    return acontrol


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


def listbox_embeddedquery():
    result = listbox()
    result.embedded_query = embedded_query()
    return result


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
    acontrol = control()
    acontrol.parent = asubform
    asubform.controls = [acontrol]
    return asubform


def subform_embeddedquery():
    asubform = subform_empty()
    asubform.embedded_query = embedded_query()
    return asubform


def form():
    asubform = subform()
    form = Form("MyForm", [asubform])
    asubform.parent = form
    return form


def form_with(control):
    asubform = subform_empty()
    control.parent = asubform
    asubform.controls.append(control)
    form = Form("FormWith", [asubform])
    asubform.parent = form
    return form


def textdoc():
    return TextDocument("plant",
                        "plant.odt",
                        "template/plant.odt", [])


def metadata_empty():
    return Metadata("testdata", [], [], [], [], [], [], [], [])


def metadata():
    meta = metadata_empty()
    plant = table_plant()
    family = table_family()
    plant.parent = family.parent = meta
    meta.table_defs.append(plant)
    meta.table_defs.append(family)
    meta.set_obj_ids()
    meta.build_parent_index()
    meta.create_index()
    return meta


def metadata_listbox():
    meta = metadata_empty()
    plant = table_plant()
    meta.table_defs.append(plant)
    alistbox = listbox()
    alistbox.link = plant.identifier
    form = form_with(alistbox)
    meta.form_defs.append(form)
    meta.set_obj_ids()
    meta.build_parent_index()
    meta.create_index()
    return meta
