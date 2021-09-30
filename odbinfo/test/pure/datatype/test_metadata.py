"tests for metadata"
import unittest

import pytest

import odbinfo.test.pure.datatype.factory as factory
from odbinfo.pure.datatype.exec import (Library, Module, PythonLibrary,
                                        PythonModule)
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import Table


class MetadataTestCase(unittest.TestCase):

    def setUp(self):
        self.meta = Metadata("testdata", [], [], [], [], [], [], [], [])

    def test_post_init(self):
        assert self.meta.index == {}
        assert self.meta.usable_by_link == {}

    def test_build_parent_index(self):
        table = Table("Plant", "All plant attributes", [], [], [])
        self.meta.table_defs = [table]

        self.meta.build_parent_index()
        assert table.parent == self.meta

    def test_basic_defs(self):
        module = Module("modname", "libname", "")
        lib = Library("lib", [module])
        self.meta.library_defs = [lib]

        assert self.meta.basicfunction_defs() == []
        assert self.meta.module_defs() == [module]

    def test_pythonmodule_defs(self):
        module = PythonModule("modname", "libname", "")
        lib = PythonLibrary("lib", [module])
        self.meta.pythonlibrary_defs = [lib]

        assert self.meta.pythonmodule_defs() == [module]

    def test_embeddedquery_defs(self):

        self.meta.report_defs = [factory.report_embeddedquery()]

        assert list(self.meta.embeddedquery_defs()) == [
            factory.embedded_query()]

    def test_commanders(self):
        report_embeddedquery = factory.report_embeddedquery()
        self.meta.report_defs = [report_embeddedquery]

        assert list(self.meta.commanders()) == [report_embeddedquery]

    def test_eventlisteners(self):
        form = factory.form()
        eventlistener = factory.eventlistener()
        self.meta.form_defs = [form]

        assert list(self.meta.eventlisteners()) == [eventlistener]

    def test_set_obj_ids(self):
        table_a = Table("Plant", "All plant attributes", [], [], [])
        table_b = Table("Family", "All family attributes", [], [], [])
        self.meta.table_defs = [table_a, table_b]

        self.meta.set_obj_ids()

        assert self.meta.obj_id == "0"
        assert table_a.obj_id == "1"
        assert table_b.obj_id == "2"
