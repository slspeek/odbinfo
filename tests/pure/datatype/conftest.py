""" factory of test objects """
from pytest import fixture

from odbinfo.pure.datatype import BasicFunction, Metadata
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.datatype.ui import (Control, DatabaseDisplay, EventListener,
                                      Form, ListBox, Report, SubForm,
                                      TextDocument)
from src.odbinfo.pure.datatype import EmbeddedQuery, Key, Table

# pylint:disable=redefined-outer-name


@fixture(scope="function")
def configuration():
    return get_configuration("test_config")


@fixture(scope="function")
def graph_config(configuration):
    return configuration.graph


@fixture(scope="function")
def basic_function_main():
    return BasicFunction("Main", "Library1", "Module1")


@fixture(scope="function")
def basic_function_notmain():
    return BasicFunction("NotMain", "Library1", "Module1")


@fixture(scope="function")
def foreignkey_family():
    return Key("myFK", [], [], "family", 3, 1, 1)


@fixture(scope="function")
def table_plant(foreignkey_family):
    plant = Table("plant", "", [foreignkey_family], [], [])
    plant.obj_id = "42"
    foreignkey_family.parent = plant
    return plant


@fixture(scope="function")
def table_family():
    return Table("family", "", [], [], [])


@fixture(scope="function")
def embedded_query():
    return EmbeddedQuery(
        "myEmbeddedQuery", "select * from Plant")


@fixture(scope="function")
def report():
    return Report("plants_report",
                  "plant",
                  "table",
                  "doc", [])


@fixture(scope="function")
def report_embeddedquery(embedded_query):
    areport = Report("plants_report",
                     "select * from plant",
                     "command",
                     "doc", [])
    areport.embedded_query = embedded_query
    return areport


@fixture(scope="function")
def eventlistener():
    return EventListener("form:performaction",
                         "vnd.sun.star.script:Library1.Module1.Main?"
                         "language=Basic&location=document")


@fixture(scope="function")
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


@fixture(scope="function")
def control(irrelevant_control, eventlistener):
    irrelevant_control.eventlisteners.append(eventlistener)
    return irrelevant_control


@fixture(scope="function")
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


@fixture(scope="function")
def listbox_embeddedquery(listbox, embedded_query):
    listbox.embedded_query = embedded_query
    return listbox


@fixture(scope="function")
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


@fixture(scope="function")
def subform(subform_empty, control):
    control.parent = subform_empty
    subform_empty.controls = [control]
    return subform_empty


@fixture(scope="function")
def subform_embeddedquery(subform_empty, embedded_query):
    subform_empty.embedded_query = embedded_query
    return subform_empty


@fixture(scope="function")
def form(subform):
    form = Form("MyForm", [subform])
    subform.parent = form
    return form


@fixture(scope="function")
def form_with_listbox(subform_empty, listbox):
    listbox.parent = subform_empty
    subform_empty.controls.append(listbox)
    form = Form("FormWith", [subform_empty])
    subform_empty.parent = form
    return form


@fixture(scope="function")
def textdoc():
    return TextDocument("plant",
                        "plant.odt",
                        "template/plant.odt", [DatabaseDisplay("id", "testdb", "plant", "table")])


@fixture(scope="function")
def metadata_empty():
    return Metadata("testdata", [], [], [], [], [], [], [], [])


@fixture(scope="function")
def metadata_tables(metadata_empty, table_plant, table_family):
    table_plant.parent = table_family.parent = metadata_empty
    metadata_empty.table_defs.append(table_plant)
    metadata_empty.table_defs.append(table_family)
    metadata_empty.set_obj_ids()
    metadata_empty.build_parent_index()
    metadata_empty.create_index()
    return metadata_empty


@fixture(scope="function")
def metadata_listbox(metadata_empty, table_plant, listbox, form_with_listbox):
    metadata_empty.table_defs.append(table_plant)
    listbox.link = table_plant.identifier
    metadata_empty.form_defs.append(form_with_listbox)

    metadata_empty.set_obj_ids()
    metadata_empty.build_parent_index()
    metadata_empty.create_index()
    return metadata_empty
