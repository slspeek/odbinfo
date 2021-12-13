"""test for graph module"""

import unittest

import pytest
from graphviz import Digraph

from odbinfo.pure.datatype.base import content_type
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.datatype.tabular import Key, Table
from odbinfo.pure.datatype.ui import Control, Form, ListBox, SubForm
from odbinfo.pure.graph import (edge, edge_attributes, generate_graphs,
                                generate_main_graph, make_dependency_edges,
                                make_edge, make_node, make_parent_edge,
                                visible_ancestor, visible_dependency_edges)


def test_is_visible_excludes_excluded(graph_config, control):
    graph_config.user_excludes = [content_type(Control)]
    assert not control.is_visible(graph_config)


def test_is_visible_excludes_included(graph_config, irrelevant_control):
    graph_config.user_excludes = []
    assert not irrelevant_control.is_visible(graph_config)


def test_is_visible_no_relevant_controls(graph_config, irrelevant_control):
    graph_config.relevant_controls = False
    assert irrelevant_control.is_visible(graph_config)


def test_is_visible_relevant_controls(graph_config, irrelevant_control):
    graph_config.relevant_controls = True
    assert not irrelevant_control.is_visible(graph_config)


def test_is_control_relevant_not_relevant_listbox(listbox):
    assert not listbox.is_relevant()


def test_is_control_relevant_listbox(listbox_embeddedquery):
    assert listbox_embeddedquery.is_relevant()


def test_is_control_relevant_control(control):
    assert control.is_relevant()


class ConfTest(unittest.TestCase):

    def setUp(self):
        self.conf = get_configuration("conftest").graph


def test_is_visible_table(table_plant, graph_config):
    assert table_plant.is_visible(graph_config)


def test_make_node_do_nothing(graph_config, digraph, table_plant):
    graph_config.user_excludes = [table_plant.content_type]
    make_node(graph_config, digraph, table_plant)
    assert len(digraph.body) == 0


class GraphTest(ConfTest):
    def setUp(self):
        super().setUp()
        self.graph = Digraph("odbinfo")


def test_make_node_name_and_id(graph_config, digraph, table_plant):
    make_node(graph_config, digraph, table_plant)

    assert len(digraph.body) == 1
    assert digraph.body[0].count("42") > 0
    assert digraph.body[0].count('id=42') > 0


def test_make_node_label(graph_config, digraph, table_plant):
    make_node(graph_config, digraph, table_plant)

    assert len(digraph.body) == 1
    assert digraph.body[0].count('label=plant') > 0


def test_make_node_tooltip(graph_config, digraph, table_plant):
    make_node(graph_config, digraph, table_plant)

    assert len(digraph.body) == 1
    assert digraph.body[0].count('tooltip="plant (table)"') > 0


def test_label_for_node(irrelevant_control):
    irrelevant_control.label = "labelvalue"
    assert irrelevant_control.graph_label == "labelvalue"


def test_no_label(irrelevant_control):
    irrelevant_control.label = ""
    assert irrelevant_control.graph_label == 'ControlName'


# visisible_ancestor
def test_edge_attributes_tooltip(graph_config, table_plant, table_family):
    assert edge_attributes(graph_config, table_plant, table_family)[
        "edgetooltip"] == "plant -> family"


def test_edge_attributes_configured_attribute(graph_config, table_plant, table_family):
    assert edge_attributes(graph_config, table_plant, table_family).items() \
        <= graph_config.relation_attrs[(content_type(Table),
                                        content_type(Table))].items()


def test_identity(table_plant, graph_config):
    assert visible_ancestor(graph_config, table_plant) == table_plant


def test_no_ancestor(graph_config, control):
    graph_config.user_excludes = [content_type(Control)]
    assert visible_ancestor(graph_config, control) is None


def test_higher_ancestor(subform, graph_config):
    control = subform.controls[0]
    graph_config.user_excludes = [content_type(Control)]
    assert visible_ancestor(graph_config, control) == subform


def test_edge(digraph, table_plant, table_family):
    table_plant.obj_id = "1"
    table_family.obj_id = "2"
    edge(digraph, table_plant, table_family, {})
    line = digraph.body[0]
    assert line == "\t1 -> 2\n"


def test_make_edge(graph_config, digraph, table_plant, table_family):
    table_plant.obj_id = "1"
    table_family.obj_id = "2"
    make_edge(graph_config, digraph, table_plant, table_family)
    line = digraph.body[0]
    assert line == """\t1 -> 2 [edgetooltip="plant -> family"]\n"""


def test_make_parent_edge_no_parent(foreignkey_family, digraph, graph_config):
    foreignkey_family.parent = None
    make_parent_edge(graph_config, digraph, foreignkey_family)
    assert len(digraph.body) == 0


def test_make_parent_edge_key_not_visible(table_plant, digraph, graph_config):
    graph_config.user_excludes = [content_type(Key)]
    make_parent_edge(graph_config, digraph, table_plant.keys[0])
    assert len(digraph.body) == 0


def test_make_parent_edge_no_visible_ancestor(graph_config, digraph, table_plant):
    graph_config.user_excludes = [content_type(Table)]
    make_parent_edge(graph_config, digraph, table_plant.keys[0])
    assert len(digraph.body) == 0


def test_make_parent_edge(graph_config, digraph, table_plant, table_family):
    graph_config.user_excludes = []
    table_plant.keys[0].obj_id = "key_id"
    table_plant.obj_id = "table_id"
    make_parent_edge(graph_config, digraph, table_plant.keys[0])
    line = digraph.body[0]
    assert line.index("\tkey_id -> table_id") > -1


# _visible_dependency_edges
def test_visible_dependency_edges_no_edges(graph_config, metadata_tables):
    assert len(visible_dependency_edges(metadata_tables, graph_config)) == 0


def test_visible_dependency_edges_one_edge(graph_config, metadata_tables):
    metadata_tables.table_defs[0].keys[0].link = metadata_tables.table_defs[1].identifier
    assert len(visible_dependency_edges(metadata_tables, graph_config)) == 1


def test_visible_dependency_edges_one_edge_no_collapse(graph_config, metadata_tables):
    graph_config.collapse_multiple_uses = False
    metadata_tables.table_defs[0].keys[0].link = metadata_tables.table_defs[1].identifier
    assert len(visible_dependency_edges(metadata_tables, graph_config)) == 1


def test_visible_dependency_edges_no_edge_user_not_visible(graph_config, metadata_listbox):
    graph_config.user_excludes = [content_type(
        ListBox), content_type(SubForm), content_type(Form)]
    assert len(visible_dependency_edges(metadata_listbox, graph_config)) == 0


def test_visible_dependency_edges_no_edge_used_not_visible(graph_config, metadata_listbox):
    graph_config.user_excludes = [content_type(Table)]
    assert len(visible_dependency_edges(metadata_listbox, graph_config)) == 0


def test_one_edge(metadata_listbox, graph_config, digraph):
    make_dependency_edges(
        metadata_listbox, graph_config, digraph)
    assert len(digraph.body) == 1


def test_generate_main_graph(configuration, metadata_listbox):
    assert len(generate_main_graph(
        metadata_listbox, configuration).body) == (2  # initial lines
                                                   + 4  # objects
                                                   + 2  # parent edges
                                                   + 1  # dependency edge
                                                   )


def test_generate_graphs(configuration, metadata_listbox):
    assert len(generate_graphs(metadata_listbox, configuration)) == 1


@pytest.mark.slow
def test_generate_main_graph_regression(metadata_processed, file_regression):
    """run generate_main_graph"""
    conf = get_configuration("test_generate_main_graph")
    file_regression.check(
        "".join(generate_main_graph(metadata_processed, conf).source))
