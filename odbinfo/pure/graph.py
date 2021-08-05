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
        return f"../{obj.type_name()}/{hugo_filename(obj.title)}/index.html"

    node = obj.parent
    while not isinstance(node, PageOwner):
        node = node.parent
    return f"../{node.type_name()}/{hugo_filename(node.title)}/index.html#{obj.obj_id}"


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


def make_edge(config: GraphConfig, graph: Digraph, start: NamedNode, end: NamedNode):
    " make edge from `start` to `end` if `config` says so "
    if not start.type_name() in config.excludes and \
            not end.type_name() in config.excludes:
        attrs = config.relation_attrs.get(
            (start.type_name(), end.type_name()), {})
        attrs["edgetooltip"] = "{} -> {}".format(start.name, end.name)
        edge(graph, start,
             end, attrs)


def make_parent_edge(config: GraphConfig, graph, node: NamedNode):
    " make edge from `node` to `parent` if `config` says so "
    if not hasattr(node, "parent"):
        return
    if not node.parent:
        return
    if not node.type_name() in config.excludes and\
            not node.parent.type_name() in config.excludes:
        attrs = {}
        attrs["edgetooltip"] = "{} is child of {}"\
            .format(node.name, node.parent.name)
        attrs["style"] = "dashed"
        attrs["color"] = "#ffcc99"
        attrs["arrowhead"] = "none"
        edge(graph, node, node.parent, attrs)


def edge(graph, start, end, attrs):
    " make an edge in `graph`"
    graph.edge(str(start.obj_id),
               str(end.obj_id),
               _attributes=attrs)


def make_dependency_edges(metadata, config, graph, node):
    " make edges for all dependencies of `node` "

    if hasattr(node, "uses"):
        if config.collapse_multiple_uses:
            uses = set(node.uses)
        else:
            uses = node.uses

        for used_node_link in uses:
            used_node = metadata.index[(
                used_node_link.object_type, used_node_link.local_id)]
            make_edge(config, graph, node, used_node)


def generate_main_graph(metadata, config):
    " returns the main graph "
    graph = Digraph(config.name)
    graph.attr("graph", rankdir="LR")
    graph.attr("graph", label=config.name,
               labelloc="top", fontsize="24")
    graph.attr("graph", tooltip="")
    for node in metadata.all_objects():
        make_node(config.graph, graph, node)
        make_parent_edge(config.graph, graph, node)
        make_dependency_edges(metadata, config.graph, graph, node)
    return graph


def generate_graphs(metadata, configuration):
    " returns a list of graphviz.Digraph objects "
    return [generate_main_graph(metadata, configuration)]
