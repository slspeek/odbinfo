""" Processor module """
import dataclasses
from typing import Sequence, Union

from odbinfo.pure.datatype import (Control, EmbeddedQuery, Form, Grid,
                                   Metadata, Module, QueryBase, SubForm)
from odbinfo.pure.datatype.base import UseAggregator, User
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.ui import AbstractCommander
from odbinfo.pure.dependency import link_name_tokens, search_dependencies
from odbinfo.pure.graph import generate_graphs
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from odbinfo.pure.parser.sql import parse
from odbinfo.pure.util import timed


def copy_tokens(module):
    """Copies the modules tokens"""
    module.tokens = [dataclasses.replace(token) for token in module.tokens]


def preprocess_module(module: Module) -> None:
    """ Tokenizes, parses, copies the tokens and sets the indexes
        of the tokens that are the names of the procedures """
    module.tokens = \
        get_basic_tokens(module.source)
    module.callables = \
        scan_basic(module.tokens, module.library, module.name)
    copy_tokens(module)
    module.name_indexes = \
        [c.name_token_index for c in module.callables]
    link_name_tokens(module)


@timed("Parse basic modules", indent=4)
def preprocess_modules(modules: Sequence[Module]) -> None:
    """preprocesses of the of libraries"""
    for module in modules:
        preprocess_module(module)


def color_hightlight_query(query: EmbeddedQuery):
    """Sets the class attribute on the special tokens"""
    for littoken in query.literal_values:
        littoken.cls = "literalvalue"


def parse_query(query: EmbeddedQuery):
    """parses `query.command`"""
    query.tokens, query.table_tokens, query.literal_values = parse(
        query.command)


@timed("Parse query", indent=6, arg=0)
def preprocess_query(query: EmbeddedQuery) -> None:
    """preprocesses `query`, that is parses it and does its the color highlighting"""
    parse_query(query)
    color_hightlight_query(query)


def set_depth(depth: int, subform: SubForm) -> None:
    """ sets depth recursively in `subform`"""
    subform.depth = depth
    for asubform in subform.subforms:
        set_depth(depth + 1, asubform)


def height(subform: SubForm) -> int:
    """ max path length to a leaf subform """
    if subform.subforms:
        return max(height(sf) for sf in subform.subforms) + 1
    return 0


def set_form_height(form: Form) -> None:
    """ set the max height into the `form` """
    form.height = max([height(sf) for sf in form.subforms], default=0)


def process_subform(subform: SubForm) -> None:
    """ simplifies control.type for all (nested) controls """

    def process_control(control: Union[Control, Grid]) -> None:
        if isinstance(control, Grid):
            return
        control.type = control.type.split(".")[-1]

    for control in subform.controls:
        process_control(control)
    for asubform in subform.subforms:
        process_subform(asubform)


@timed("Process form", arg=0, indent=6)
def preprocess_form(form: Form) -> None:
    """ calculate depth for its subforms """
    for subform in form.subforms:
        set_depth(0, subform)
        process_subform(subform)
    set_form_height(form)


def aggregate_uses_from_children(user_agg: UseAggregator) -> None:
    """Collect aggregated uses from its children """
    for user in user_agg.all_objects():
        if isinstance(user, User) and user.link:
            user_agg.uses.append(user.link)


@timed("Aggregate uses", indent=4)
def aggregate_uses(metadata: Metadata) -> None:
    """Collect all aggregated uses """
    for use_agg in metadata.all_objects():
        if isinstance(use_agg, UseAggregator):
            aggregate_uses_from_children(use_agg)


def aggregate_used_by(metadata: Metadata) -> None:
    """Collect all used_by"""
    for user in metadata.all_active_users:
        metadata.usable_by_link[user.link].used_by.append(user.identifier)


@timed("Parse queries", indent=4)
def preprocess_queries(metadata: Metadata) -> None:
    """process all query-like objects"""
    for query in metadata.by_content_type(QueryBase):
        preprocess_query(query)


def preprocess_commanders(commanders: Sequence[AbstractCommander]) -> None:
    """ if command is a direct query, set an EmbeddedQuery obj"""
    for cmdr in commanders:
        if cmdr.issqlcommand:
            cmdr.embedded_query = \
                EmbeddedQuery(f"{cmdr.name}.Command", cmdr.command)


def preprocess_forms(form_defs: Sequence[Form]):
    """preprocesses all forms in `form_defs`"""
    for form in form_defs:
        preprocess_form(form)


@timed("Process metadata", indent=2)
def process_metadata(config: Configuration, metadata: Metadata) -> Metadata:
    """ preprocessing of the data before it is written """
    preprocess_modules(metadata.module_defs)
    for module in metadata.module_defs:
        link_name_tokens(module)

    preprocess_commanders(metadata.commanders)
    preprocess_queries(metadata)
    preprocess_forms(metadata.form_defs)

    metadata.prepare_indexed_tree()

    # TODO move these 3 lines to dependency module
    search_dependencies(metadata)
    aggregate_uses(metadata)
    aggregate_used_by(metadata)

    metadata.graphs = generate_graphs(metadata, config)
    metadata.set_parent_links(None)
    # for test purposes only
    return metadata
