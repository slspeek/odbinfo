"test for graph module"

import unittest

import pytest

from odbinfo.pure.datatype import Control, content_type
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.graph import (_is_control_visible, generate_main_graph, href,
                                hugo_filename, is_visible, visible_edges)
from odbinfo.test.pure.datatype import factory
from odbinfo.test.pure.fixtures import metadata_processed


@pytest.mark.slow
def test_visible_edges(metadata_processed, data_regression):
    conf = get_configuration().graph
    data_regression.check(visible_edges(metadata_processed, conf))


class HugoFilename(unittest.TestCase):
    def setUp(self):
        pass

    def test_to_lower(self):
        assert hugo_filename("Foo") == "foo"

    def test_spaces(self):
        assert hugo_filename("F oo") == "f-oo"


class Href(unittest.TestCase):

    def test_webpage(self):
        assert href(factory.table_plant()) == \
            "../table/plant/index.html"

    def test_control(self):
        form = factory.form()
        subform = form.subforms[0]
        subform.parent = form
        subform.obj_id = "42"
        assert href(subform) == \
            "../form/myform/index.html#42"


class ConfTest(unittest.TestCase):
    def setUp(self):
        self.conf = get_configuration().graph


class IsVisibleExcludes(ConfTest):
    def setUp(self):
        super().setUp()
        self.node = Control("control1", "c1", None, False, True,
                            "Label", "otherControl", "text", [])

    def test_excluded(self):
        self.conf.user_excludes = [content_type(Control)]
        assert not is_visible(self.conf, self.node)

    def test_included(self):
        self.conf.user_excludes = []
        assert not is_visible(self.conf, self.node)


class IsVisibleControl(ConfTest):

    def setUp(self):
        super().setUp()
        self.irrelevant_node = Control("control1", "c1", None, False, True,
                                       "Label", "otherControl", "text", [])

    def test_no_relevant_controls(self):
        self.conf.relevant_controls = False
        assert is_visible(self.conf, self.irrelevant_node)

    def test_relevant_controls(self):
        self.conf.relevant_controls = True
        assert not is_visible(self.conf, self.irrelevant_node)


class IsControlVisible(unittest.TestCase):

    def test_not_visible_listbox(self):
        self.listbox = factory.listbox()
        assert not _is_control_visible(self.listbox)

    def test_visible_listbox(self):
        self.listbox = factory.listbox_embeddedquery()
        assert _is_control_visible(self.listbox)

    def test_visible_control(self):
        self.relevant_control = factory.control()
        assert _is_control_visible(self.relevant_control)


class IsVisibleOtherTypes(ConfTest):

    def setUp(self):
        super().setUp()
        self.node = factory.table_plant()

    def test_table(self):
        assert is_visible(self.conf, self.node)


@pytest.mark.slow
def test_visible_edges_no_collapse(metadata_processed):
    conf = get_configuration().graph
    conf.collapse_multiple_uses = False
    conf.excludes.append("table")
    visible_edges(metadata_processed, conf)


@pytest.mark.slow
def test_visible_edges_tables_excluded(metadata_processed):
    "tables excluded"
    conf = get_configuration().graph
    conf.excludes.append("table")
    visible_edges(metadata_processed, conf)


@pytest.mark.slow
def test_generate_main_graph(metadata_processed):
    "run generate_main_graph with relevant_controls off for coverage"
    conf = get_configuration()
    conf.name = "test_generate_main_graph"
    conf.graph.relevant_controls = False
    generate_main_graph(metadata_processed, conf)
