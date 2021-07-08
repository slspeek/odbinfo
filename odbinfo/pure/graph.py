" Graphviz graph generation "
from typing import cast

from graphviz import Digraph

from odbinfo.pure.datatype import Control, PageOwner
from odbinfo.pure.datatype.base import NamedNode
from odbinfo.pure.datatype.config import GraphConfig


def hugo_filename(name: str) -> str:
    " name converted as hugo converts filename to .Params.filename "
    return name.replace(" ", "-").lower()


def href(obj):
    """ returns a href html attribute """
    if isinstance(obj, PageOwner):
        return f"../{obj.type_name()}/{hugo_filename(obj.title)}"

    node = obj.parent
    while not isinstance(node, PageOwner):
        node = node.parent
    return f"../{node.type_name()}/{hugo_filename(node.title)}/#{obj.obj_id}"


def make_node(config: GraphConfig,
              graph: Digraph, node: NamedNode):
    " adds a node to `graph` for `node` if `config` says so "
    if not node.type_name() in config.excludes:
        label = node.name
        if node.type_name() == "control":
            control = cast(Control, node)
            if control.label:
                label = control.label
        graph.node(str(node.obj_id),
                   label=label,
                   tooltip="{} ({})".format(node.name,
                                            node.type_name()),
                   href=href(node),
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
    return graph


def generate_graphs(metadata, configuration):
    " returns a list of graphviz.Digraph objects "
    return [generate_main_graph(metadata, configuration)]
