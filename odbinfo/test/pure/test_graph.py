"""test for graph module"""

import unittest

import pytest
from graphviz import Digraph

from odbinfo.pure.datatype import (Control, Form, Key, ListBox, SubForm, Table,
                                   content_type)
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.graph import (_is_control_visible, edge, edge_attributes,
                                generate_graphs, generate_main_graph, href,
                                hugo_filename, is_visible,
                                make_dependency_edges, make_edge, make_node,
                                make_parent_edge, visible_ancestor,
                                visible_dependency_edges)
from odbinfo.test.pure.datatype import factory
from odbinfo.test.pure.fixtures import metadata_processed


def test_hugo_filename_to_lower():
    assert hugo_filename("Foo") == "foo"


def test__hugo_filename_spaces():
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
        self.conf = get_configuration("conftest").graph


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


class MakeNodeInvisibleNode(ConfTest):
    def setUp(self):
        super().setUp()
        self.node = factory.table_plant()
        self.conf.user_excludes = [self.node.content_type()]
        self.graph = Digraph("odbinfo")

    def test_do_nothing(self):
        make_node(self.conf, self.graph, self.node)
        assert len(self.graph.body) == 0


class GraphTest(ConfTest):
    def setUp(self):
        super().setUp()
        self.graph = Digraph("odbinfo")


class MakeNodeVisibleNode(GraphTest):

    def setUp(self):
        super().setUp()
        self.node = factory.table_plant()
        self.node.obj_id = "42"

    def test_name_and_id(self):
        make_node(self.conf, self.graph, self.node)

        assert len(self.graph.body) == 1
        assert self.graph.body[0].index("42") > -1
        assert self.graph.body[0].index('id=42') > -1

    def test_label(self):
        make_node(self.conf, self.graph, self.node)

        assert len(self.graph.body) == 1
        assert self.graph.body[0].index('label=plant') > -1

    def test_tooltip(self):
        make_node(self.conf, self.graph, self.node)

        assert len(self.graph.body) == 1
        assert self.graph.body[0].index('tooltip="plant (table)"') > -1


class MakeNodeVisibleControlLabel(ConfTest):

    def setUp(self):
        super().setUp()
        self.form = factory.form()
        self.node = self.form.subforms[0].controls[0]

        self.node.obj_id = "42"
        self.node.label = "labelvalue"
        self.graph = Digraph("odbinfo")

    def test_label(self):
        make_node(self.conf, self.graph, self.node)

        assert len(self.graph.body) == 1
        assert self.graph.body[0].index('label=labelvalue') > -1

    def test_no_label(self):
        self.node.label = ""
        make_node(self.conf, self.graph, self.node)

        assert len(self.graph.body) == 1
        assert self.graph.body[0].index('label=ControlName') > -1


class VisibleAncestor(ConfTest):

    def test_identity(self):
        self.webpage = factory.table_plant()
        assert visible_ancestor(self.conf, self.webpage) == self.webpage

    def test_no_ancestor(self):
        self.control = factory.control()
        self.conf.user_excludes = [content_type(Control)]
        assert visible_ancestor(self.conf, self.control) is None

    def test_higher_ancestor(self):
        self.subform = factory.subform()
        self.control = self.subform.controls[0]
        self.conf.user_excludes = [content_type(Control)]
        assert visible_ancestor(self.conf, self.control) == self.subform


class EdgeAttributes(ConfTest):
    def setUp(self):
        super().setUp()
        self.start = factory.table_plant()
        self.end = factory.table_family()

    def test_tooltip(self):
        assert edge_attributes(self.conf, self.start, self.end)[
            "edgetooltip"] == "plant -> family"

    def test_configured_attribute(self):
        assert edge_attributes(self.conf, self.start, self.end).items() \
            <= self.conf.relation_attrs[(content_type(Table),
                                         content_type(Table))].items()


class Edge(GraphTest):

    def setUp(self):
        super().setUp()
        self.start = factory.table_plant()
        self.start.obj_id = "1"
        self.end = factory.table_family()
        self.end.obj_id = "2"

    def test_edge(self):
        edge(self.graph, self.start, self.end, {})
        line = self.graph.body[0]
        assert line == "\t1 -> 2\n"


class MakeEdge(Edge):

    def test_edge(self):
        make_edge(self.conf, self.graph, self.start, self.end)
        line = self.graph.body[0]
        assert line == """\t1 -> 2 [edgetooltip="plant -> family"]\n"""


class MakeParentEdge(GraphTest):
    def setUp(self):
        super().setUp()
        self.conf.user_excludes = []
        self.plant = factory.table_plant()
        self.plant.obj_id = "table_id"

        self.key = self.plant.keys[0]
        self.key.obj_id = "key_id"

    def test_no_parent(self):
        self.key.parent = None
        make_parent_edge(self.conf, self.graph, self.key)
        assert len(self.graph.body) == 0

    def test_key_not_visible(self):
        self.conf.user_excludes = [content_type(Key)]
        make_parent_edge(self.conf, self.graph, self.key)
        assert len(self.graph.body) == 0

    def test_no_visible_ancestor(self):
        self.conf.user_excludes = [content_type(Table)]
        make_parent_edge(self.conf, self.graph, self.key)
        assert len(self.graph.body) == 0

    def test_edge(self):
        make_parent_edge(self.conf, self.graph, self.key)
        line = self.graph.body[0]
        assert line.index("\tkey_id -> table_id") > -1
        assert len(self.conf.parent_edge_attrs.items()) == 3


class VisibleDependencyEdges(ConfTest):

    def setUp(self):
        super().setUp()
        self.meta = factory.metadata()

    def test_no_edges(self):
        assert len(visible_dependency_edges(self.meta, self.conf)) == 0

    def test_one_edge(self):
        self.meta.table_defs[0].keys[0].link = self.meta.table_defs[1].identifier
        assert len(visible_dependency_edges(self.meta, self.conf)) == 1

    def test_one_edge_no_collapse(self):
        self.conf.collapse_multiple_uses = False
        self.test_one_edge()


class VisibleDependencyEdgesNoVisibleAncestor(ConfTest):

    def setUp(self):
        super().setUp()
        self.meta = factory.metadata_listbox()

    def test_no_edge_user_not_visible(self):
        self.conf.user_excludes = [content_type(
            ListBox), content_type(SubForm), content_type(Form)]
        assert len(visible_dependency_edges(self.meta, self.conf)) == 0

    def test_no_edge_used_not_visible(self):
        self.conf.user_excludes = [content_type(Table)]
        assert len(visible_dependency_edges(self.meta, self.conf)) == 0


class MakeDepencyEdges(GraphTest):

    def setUp(self):
        super().setUp()
        self.meta = factory.metadata_listbox()

    def test_one_edge(self):
        make_dependency_edges(
            self.meta, self.conf, self.graph)
        assert len(self.graph.body) == 1


class GenerateMainGraph(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.meta = factory.metadata_listbox()
        self.conf = get_configuration("testrun")

    def test_generate_main_graph(self):
        self.graph = generate_main_graph(
            self.meta, self.conf)
        # print(self.graph.source)
        assert len(self.graph.body) == (2  # initial lines
                                        + 4  # objects
                                        + 2  # parent edges
                                        + 1  # dependency edge
                                        )


class GenerateGraphs(GenerateMainGraph):

    def test_generate_graphs(self):
        graphs = generate_graphs(self.meta, self.conf)
        assert len(graphs) == 1


@pytest.mark.slow
def test_generate_main_graph(metadata_processed, data_regression):
    """run generate_main_graph"""
    conf = get_configuration("test_generate_main_graph")
    data_regression.check(generate_main_graph(metadata_processed, conf).source)
