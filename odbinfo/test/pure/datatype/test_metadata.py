"tests for metadata"
import pytest

from odbinfo.pure.datatype.exec import (Library, Module, PythonLibrary,
                                        PythonModule)
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import Table
from odbinfo.test.pure.datatype.test_ui import (EMBEDDED_QUERY, EVENTLISTENER,
                                                FORM, REPORT_EMBEDDEDQUERY)


def test_post_init():
    meta = Metadata("testdata", [], [], [], [], [], [], [], [])
    assert meta.index == {}
    assert meta.usable_by_link == {}


def test_build_parent_index():
    table = Table("Plant", "All plant attributes", [], [], [])
    meta = Metadata("testdata", [table], [], [], [], [], [], [], [])

    meta.build_parent_index()
    assert table.parent == meta


def test_basic_defs():
    module = Module("modname", "libname", "")
    lib = Library("lib", [module])
    meta = Metadata("testdata", [], [], [], [], [], [lib], [], [])

    assert meta.basicfunction_defs() == []
    assert meta.module_defs() == [module]


def test_pythonmodule_defs():
    module = PythonModule("modname", "libname", "")
    lib = PythonLibrary("lib", [module])
    meta = Metadata("testdata", [], [], [], [], [], [], [lib], [])

    assert meta.pythonmodule_defs() == [module]


def test_embeddedquery_defs():
    meta = Metadata("testdata", [], [], [], [], [
                    REPORT_EMBEDDEDQUERY], [], [], [])
    assert list(meta.embeddedquery_defs()) == [EMBEDDED_QUERY]


def test_commanders():
    meta = Metadata("testdata", [], [], [], [], [
                    REPORT_EMBEDDEDQUERY], [], [], [])
    assert list(meta.commanders()) == [REPORT_EMBEDDEDQUERY]


def test_eventlisteners():
    meta = Metadata("testdata", [], [], [], [FORM], [], [], [], [])
    assert list(meta.eventlisteners()) == [EVENTLISTENER]


def test_set_obj_ids():
    table_a = Table("Plant", "All plant attributes", [], [], [])
    table_b = Table("Family", "All family attributes", [], [], [])

    meta = Metadata("testdata", [table_a, table_b], [], [], [], [], [], [], [])
    meta.set_obj_ids()
    assert meta.obj_id == "0"
    assert table_a.obj_id == "1"
    assert table_b.obj_id == "2"
