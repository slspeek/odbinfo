""" Graphviz graph generation """
from typing import Dict, Sequence, Tuple

from graphviz import Digraph

from odbinfo.pure.datatype import base
from odbinfo.pure.datatype.base import NamedNode
from odbinfo.pure.datatype.config import Configuration, GraphConfig
from odbinfo.pure.datatype.metadata import Metadata


def create_node(config: GraphConfig, graph: Digraph, node: NamedNode):
    """ adds a node to `graph` for `node` if `config` says so.
     """
    if node.is_visible(config):
        graph.node(str(node.obj_id),
                   label=node.graph_label,
                   tooltip=f"{node.name} ({node.content_type})",
                   href=node.href,
                   id=node.obj_id,
                   _attributes=config.type_attrs.get(node.content_type, {}))


def visible_ancestor(config: GraphConfig, node):
    """ returns `node` if `node` is visible, else the first ancestor that is visible
        or None if there is no visible ancestor"""
    parent = node
    while not parent.is_visible(config):
        parent = parent.parent
        if not parent:
            return None
    return parent


def edge_attributes(config: GraphConfig, from_node: NamedNode,
                    to_node: NamedNode) -> Dict[str, str]:
    """composes the node attributes"""
    attrs = config.relation_attrs.get(from_node.content_type,
                                      {}).get(to_node.content_type, {})
    attrs["edgetooltip"] = f"{from_node.name} -> {to_node.name}"
    return attrs


def create_edge(graph, from_node, to_node, attrs):
    """ make an edge in `graph`"""
    graph.edge(from_node.obj_id, to_node.obj_id, _attributes=attrs)


def create_parent_edge(config: GraphConfig, graph, node: NamedNode):
    """ make edge from `node` to `parent` if `config` says so """
    if not node.parent:
        return
    if node.is_visible(config):
        avisible_ancestor = visible_ancestor(config, node.parent)
        if not avisible_ancestor:
            return

        attrs = dict(config.parent_edge_attrs)
        attrs["edgetooltip"] = \
            f"{node.name} is child of {avisible_ancestor.name}"

        create_edge(graph, node, avisible_ancestor, attrs)


def visible_dependency_edges(metadata: Metadata, config: GraphConfig) \
        -> Sequence[Tuple[str, str]]:
    """ returns edges to draw in graph """
    uses = []
    for user in metadata.actual_users:
        used_node = metadata.usable_by_link[user.link]
        user_vis_ancestor = visible_ancestor(config, user)
        if not user_vis_ancestor:
            continue
        used_vis_ancestor = visible_ancestor(config, used_node)
        if not used_vis_ancestor:
            continue
        uses.append((user_vis_ancestor.obj_id, used_vis_ancestor.obj_id))
    if config.collapse_multiple_uses:
        return list(dict.fromkeys(uses))
    return uses


def create_dependency_edges(metadata: Metadata, config: GraphConfig,
                            graph: Digraph):
    """ make edges for all dependencies """
    uses = visible_dependency_edges(metadata, config)
    for use in uses:
        start = metadata.node_by_id[use[0]]
        end = metadata.node_by_id[use[1]]
        create_edge(graph, start, end, edge_attributes(config, start, end))


def create_digraph(name: str) -> Digraph:
    """ Creates an empty graphviz.Digraph with `name` and sets some graph attributes"""
    graph = Digraph(name, filename=f"{base.hugo_filename(name)}.gv")
    graph.attr("graph", rankdir="LR")
    graph.attr("graph", label=name, labelloc="top", fontsize="24")
    return graph


def generate_main_graph(metadata: Metadata, config: Configuration) -> Digraph:
    """ returns the main graph with all nodes from `metadata` if not excluded in `config`
        and the edges between them"""
    graph = create_digraph(config.name)
    for node in metadata.all_objects():
        create_node(config.graph, graph, node)
        create_parent_edge(config.graph, graph, node)
    create_dependency_edges(metadata, config.graph, graph)
    return graph
