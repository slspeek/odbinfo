""" Processor module """
import dataclasses
from typing import Sequence, Union

from odbinfo.pure.datatype import (Control, EmbeddedQuery, Form, Grid, Library,
                                   Metadata, Module, SubForm)
from odbinfo.pure.datatype.base import UseAggregator, User
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.dependency import link_name_tokens, search_dependencies
from odbinfo.pure.graph import generate_graphs
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from odbinfo.pure.parser.sql import parse
from odbinfo.pure.util import timed


def copy_tokens(module):
    """Copies the modules tokens"""
    module.tokens = [dataclasses.replace(token) for token in module.tokens]


def _process_library(library: Library) -> None:
    def parse_module(module: Module) -> None:
        # print("parsing: " + module.source)
        module.tokens = \
            get_basic_tokens(module.source)
        module.callables = \
            scan_basic(module.tokens, library.name, module.name)
        copy_tokens(module)
        module.name_indexes = \
            [c.name_token_index for c in module.callables]

    for module in library.modules:
        parse_module(module)


@timed("Parse basic libraries", indent=4)
def _process_libraries(libraries: Sequence[Library]) -> None:
    for lib in libraries:
        _process_library(lib)


@timed("Parse query", indent=6, arg=0)
def _process_query(query: EmbeddedQuery) -> None:
    query.tokens, query.table_tokens, query.literal_values = parse(
        query.command)
    for littoken in query.literal_values:
        littoken.cls = "literalvalue"


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
def process_form(form: Form) -> None:
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
    for user in metadata.all_active_users():
        metadata.usable_by_link[user.link].used_by.append(user.identifier)


@timed("Parse queries", indent=4)
def process_queries(metadata: Metadata) -> None:
    """process all query-like objects"""
    for query in metadata.query_defs:
        _process_query(query)
    for view in metadata.view_defs:
        _process_query(view)
    for embedded_query in metadata.embeddedquery_defs():
        _process_query(embedded_query)


def preprocess_commanders(metadata: Metadata) -> None:
    """ if command is a direct query, set an EmbeddedQuery obj"""
    for cmdr in metadata.commanders():
        if cmdr.issqlcommand:
            cmdr.embedded_query = \
                EmbeddedQuery(f"{cmdr.name}.Command", cmdr.command)


@timed("Process metadata", indent=2)
def process_metadata(config: Configuration, metadata: Metadata) -> Metadata:
    """ preprocessing of the data before it is send to hugo """
    preprocess_commanders(metadata)
    _process_libraries(metadata.library_defs)
    process_queries(metadata)

    for form in metadata.form_defs:
        process_form(form)

    metadata.set_parent_links(None)
    metadata.build_parent_index()
    metadata.set_obj_ids()
    for module in metadata.module_defs():
        link_name_tokens(module)

    # TODO move these 4 lines to dependency module
    search_dependencies(metadata)
    metadata.create_index()
    aggregate_uses(metadata)
    aggregate_used_by(metadata)

    metadata.graphs = generate_graphs(metadata, config)
    # for test purposes only
    return metadata
