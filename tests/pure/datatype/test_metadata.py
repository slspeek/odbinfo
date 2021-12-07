"""tests for metadata"""

from odbinfo.pure.datatype import Library, Module, PythonLibrary, PythonModule


def test_metadata_post_init(metadata_empty):
    assert metadata_empty.node_by_id == {}
    assert metadata_empty.usable_by_link == {}


def test_metadata_build_parent_index(table_plant, metadata_empty):
    metadata_empty.table_defs = [table_plant]

    metadata_empty._set_parents()
    assert table_plant.parent == metadata_empty


def test_basic_defs(metadata_empty):
    module = Module("modname", "libname", "")
    lib = Library("lib", [module])
    metadata_empty.library_defs = [lib]

    assert metadata_empty.basicfunction_defs == []
    assert metadata_empty.module_defs == [module]


def test_pythonmodule_defs(metadata_empty):
    module = PythonModule("modname", "libname", "")
    lib = PythonLibrary("lib", [module])
    metadata_empty.pythonlibrary_defs = [lib]

    assert metadata_empty.pythonmodule_defs == [module]


def test_embeddedquery_defs(metadata_empty, report_embeddedquery, embedded_query):
    metadata_empty.report_defs = [report_embeddedquery]
    assert list(metadata_empty.embeddedqueries) == [
        embedded_query]


def test_commanders(metadata_empty, report_embeddedquery):
    metadata_empty.report_defs = [report_embeddedquery]
    assert list(metadata_empty.commanders) == [report_embeddedquery]


def test_eventlisteners(metadata_empty, form, eventlistener):
    metadata_empty.form_defs = [form]

    assert list(metadata_empty.eventlisteners) == [eventlistener]


def test_set_obj_ids(metadata_empty, table_plant, table_family):
    metadata_empty.table_defs = [table_plant, table_family]

    metadata_empty._set_obj_ids()

    assert metadata_empty.obj_id == "0"
    assert table_plant.obj_id == "1"
    assert table_plant.keys[0].obj_id == "2"
    assert table_family.obj_id == "3"


def test_create_index(metadata_empty, table_plant, table_family):
    metadata_empty.table_defs = [table_plant, table_family]
    metadata_empty._set_obj_ids()
    metadata_empty._create_index()
    assert metadata_empty.node_by_id["1"] == table_plant
    assert metadata_empty.node_by_id["3"] == table_family
    assert metadata_empty.usable_by_link[table_plant.identifier] == table_plant
    assert metadata_empty.usable_by_link[table_family.identifier] == table_family


def test_all_active_users(metadata_tables):
    key = metadata_tables.table_defs[0].keys[0]
    key.link = metadata_tables.table_defs[1].identifier

    active_users = list(metadata_tables.all_active_users)
    assert len(active_users) == 1
    assert key in active_users
