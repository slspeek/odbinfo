""" Graphviz graph generation """
from typing import Dict, Sequence, Tuple, cast

from graphviz import Digraph

from odbinfo.pure.datatype import Control, ListBox, Metadata, content_type
from odbinfo.pure.datatype.base import NamedNode, Node
from odbinfo.pure.datatype.config import GraphConfig


def hugo_filename(name: str) -> str:
    """ name converted as hugo converts filename to .Params.filename """
    return name.replace(" ", "-").lower()


def href(obj: Node) -> str:
    """ returns a href html attribute """
    link = obj.identifier
    url = f"../{link.content_type}/{hugo_filename(link.local_id)}/index.html"
    if link.bookmark:
        url = f"{url}#{link.bookmark}"
    return url


def _is_control_visible(control: Control) -> bool:
    if control.eventlisteners:
        return True
    if isinstance(control, ListBox):
        listbox = cast(ListBox, control)
        if listbox.embedded_query or listbox.link:
            return True
    return False


def is_visible(config: GraphConfig, node: NamedNode) -> bool:
    """ determines with `config` whether `node` is visible"""
    if not node.content_type() in config.excludes:
        if config.relevant_controls:
            if isinstance(node, Control):
                control = cast(Control, node)
                return _is_control_visible(control)
            return True
        return True
    return False


def make_node(config: GraphConfig,
              graph: Digraph, node: NamedNode):
    """ adds a node to `graph` for `node` if `config` says so """
    if is_visible(config, node):
        label = node.name
        if node.content_type() == content_type(Control):
            control = cast(Control, node)
            if control.label:
                label = control.label
        graph.node(str(node.obj_id),
                   label=label,
                   tooltip=f"{node.name} ({node.content_type()})",
                   href=href(node),
                   id=node.obj_id,
                   _attributes=config.type_attrs.get(node.content_type(), {}))


def visible_ancestor(config: GraphConfig, node):
    """ returns `node` if is visible, else first ancestor that is visible
        or None if there is no visible ancestor"""
    parent = node
    while not is_visible(config, parent):
        parent = parent.parent
        if not parent:
            return None
    return parent


def edge_attributes(config: GraphConfig,
                    start: NamedNode, end: NamedNode) -> Dict[str, str]:
    """composes the node attributes"""
    attrs = config.relation_attrs.get(
        (start.content_type(), end.content_type()), {})
    attrs["edgetooltip"] = f"{start.name} -> {end.name}"
    return attrs


def edge(graph, start, end, attrs):
    """ make an edge in `graph`"""
    graph.edge(start.obj_id,
               end.obj_id,
               _attributes=attrs)


def make_edge(config: GraphConfig, graph: Digraph, start: NamedNode, end: NamedNode):
    """ make edge from `start` to `end` with attributes specified by `config`"""

    edge(graph, start,
         end, edge_attributes(config, start, end))


def make_parent_edge(config: GraphConfig, graph, node: NamedNode):
    """ make edge from `node` to `parent` if `config` says so """
    if not node.parent:
        return
    if is_visible(config, node):
        avisible_ancestor = visible_ancestor(config, node.parent)
        if not avisible_ancestor:
            return

        attrs = dict(config.parent_edge_attrs)
        attrs["edgetooltip"] =\
            f"{node.name} is child of {avisible_ancestor.name}"

        edge(graph, node, avisible_ancestor, attrs)


def visible_dependency_edges(metadata: Metadata, config: GraphConfig) \
        -> Sequence[Tuple[str, str]]:
    """ returns edges to draw in graph """
    uses = []
    for user in metadata.all_active_users():
        # print("In: from:", user.title, " to ", user.link)
        used_node_link = user.link
        used_node = metadata.usable_by_link[
            used_node_link]
        user_vis_ancestor = visible_ancestor(config, user)
        if not user_vis_ancestor:
            continue
        used_vis_ancestor = visible_ancestor(config, used_node)
        if not used_vis_ancestor:
            continue
        # print("Out: from:", user_vis_ancestor.title,
        #       " to ", used_vis_ancestor.title)
        uses.append((user_vis_ancestor.obj_id,
                     used_vis_ancestor.obj_id))
    if config.collapse_multiple_uses:
        return list(dict.fromkeys(uses))
    return uses


def make_dependency_edges(metadata, config, graph):
    """ make edges for all dependencies """
    uses = visible_dependency_edges(metadata, config)
    for use in uses:
        start = metadata.index[use[0]]
        end = metadata.index[use[1]]
        make_edge(config, graph, start, end)


def generate_main_graph(metadata, config):
    """ returns the main graph """
    graph = Digraph(config.name)
    graph.attr("graph", rankdir="LR")
    graph.attr("graph", label=config.name,
               labelloc="top", fontsize="24")
    # graph.attr("graph", tooltip="")
    for node in metadata.all_objects():
        make_node(config.graph, graph, node)
        make_parent_edge(config.graph, graph, node)

    make_dependency_edges(metadata, config.graph, graph)
    return graph


def generate_graphs(metadata, configuration):
    """ returns a list of graphviz.Digraph objects """
    return [generate_main_graph(metadata, configuration)]
