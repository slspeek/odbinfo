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


def visible_ancestor(config: GraphConfig, node):
    """ returns `node` if is visible, else first ancestor that is visible
        or None if there is no visible ancestor"""
    parent = node
    while parent.type_name() in config.excludes:
        parent = parent.parent
        if not parent:
            return None
    return parent


def make_edge(config: GraphConfig, graph: Digraph, start: NamedNode, end: NamedNode):
    " make edge from `start` to `end` with attributes specified by `config`"
    attrs = config.relation_attrs.get(
        (start.type_name(), end.type_name()), {})
    attrs["edgetooltip"] = "{} -> {}".format(
        start.title, end.title)
    edge(graph, start,
         end, attrs)


def make_parent_edge(config: GraphConfig, graph, node: NamedNode):
    " make edge from `node` to `parent` if `config` says so "
    if not hasattr(node, "parent"):
        return
    if not node.parent:
        return
    if not node.type_name() in config.excludes:
        avisible_ancestor = visible_ancestor(config, node.parent)
        if not avisible_ancestor:
            return

        attrs = {}
        attrs["edgetooltip"] = "{} is child of {}"\
            .format(node.name, avisible_ancestor.name)
        attrs["style"] = "dashed"
        attrs["color"] = "#ffcc99"
        attrs["arrowhead"] = "none"
        edge(graph, node, avisible_ancestor, attrs)


def edge(graph, start, end, attrs):
    " make an edge in `graph`"
    graph.edge(str(start.obj_id),
               str(end.obj_id),
               _attributes=attrs)


def visible_edges(metadata, config):
    " returns edges to draw in graph "
    uses = []
    for user in metadata.all_active_users():
        # print("In: from:", user.title, " to ", user.link)
        used_node_link = user.link
        used_node = metadata.index[(
            used_node_link.object_type, used_node_link.local_id)]
        user_vis_ancestor = visible_ancestor(config, user)
        if not user_vis_ancestor:
            continue
        used_vis_ancestor = visible_ancestor(config, used_node)
        if not used_vis_ancestor:
            continue
        # print("Out: from:", user_vis_ancestor.title,
        #       " to ", used_vis_ancestor.title)
        uses.append(((user_vis_ancestor.type_name(), user_vis_ancestor.title),
                     (used_vis_ancestor.type_name(), used_vis_ancestor.title)))
    if config.collapse_multiple_uses:
        uses = set(uses)
    return uses


def make_dependency_edges(metadata, config, graph):
    " make edges for all dependencies of `node` "
    uses = visible_edges(metadata, config)
    for use in uses:
        start = metadata.index[use[0]]
        end = metadata.index[use[1]]
        make_edge(config, graph, start, end)


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

    make_dependency_edges(metadata, config.graph, graph)
    return graph


def generate_graphs(metadata, configuration):
    " returns a list of graphviz.Digraph objects "
    return [generate_main_graph(metadata, configuration)]
