"tests for metadata"
import unittest

import pytest

import odbinfo.test.pure.datatype.factory as factory
from odbinfo.pure.datatype.base import Token
from odbinfo.pure.datatype.exec import (Library, Module, PythonLibrary,
                                        PythonModule)
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import Query, Table


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


class CreateIndexTest(MetadataTestCase):

    def setUp(self):
        super().setUp()
        self.table_a = Table("Plant", "All plant attributes", [], [], [])
        self.table_b = Table("Family", "All family attributes", [], [], [])
        self.meta.table_defs = [self.table_a, self.table_b]

    def test_create_index(self):
        self.meta.set_obj_ids()
        self.meta.create_index()
        assert self.meta.index["1"] == self.table_a
        assert self.meta.index["2"] == self.table_b
        assert self.meta.usable_by_link[self.table_a.identifier] == self.table_a
        assert self.meta.usable_by_link[self.table_b.identifier] == self.table_b


class AllActiveUsersTest(CreateIndexTest):

    def setUp(self):
        super().setUp()
        self.token = Token("Plant", 0, 0, False)
        self.token.link = self.table_a.identifier
        self.query = Query("myquery", "select * from Plant")
        self.query.tokens.append(self.token)
        self.meta.query_defs = [self.query]

    def test_all_active_users(self):
        active_users = list(self.meta.all_active_users())
        assert len(active_users) == 1
        assert self.token in active_users
        assert self.token in active_users
