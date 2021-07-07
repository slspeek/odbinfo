" Graphviz graph generation "
from typing import cast

from graphviz import Digraph

from odbinfo.pure.datatype import Control
from odbinfo.pure.datatype.base import NamedNode
from odbinfo.pure.datatype.config import GraphConfig


def href(config, obj):
    """ returns the value for a href html attribute """
    file = config.type_href[obj.type_name()]
    return "../{}.html#{}".format(file, obj.obj_id)


def make_node(config: GraphConfig, graph: Digraph, node: NamedNode):
    " adds a node to `graph` for `node` if `config` says so "
    if not node.type_name() in config.excludes:
        if node.type_name() == "control":
            label = cast(Control, node).label
        else:
            label = node.name
        graph.node(str(node.obj_id),
                   label=label,
                   tooltip="{} ({})".format(node.name,
                                            node.type_name()),
                   href=href(config, node),
                   id=node.obj_id,
                   _attributes=config.type_attrs[node.type_name()])


# pylint:disable=unused-argument
def generate_main_graph(metadata, config):
    " returns the main graph "
    graph = Digraph(config.name)
    graph.attr("graph", rankdir="LR")
    graph.attr("graph", label=config.name,
               labelloc="top", fontsize="24")
    for node in metadata.all_objects():
        make_node(config.graph, graph, node)
    print(f"{config.general.output_dir}/{config.name}")
    # graph.view()
    # move to writer.py
    # graph.save(directory=f"{config.general.output_dir}/{config.name}")
    # graph.render(format="svg")
    return graph


def generate_graphs(metadata, configuration):
    " returns a list of graphviz.Digraph objects "
    return [generate_main_graph(metadata, configuration)]
