""" test dependency search in tabulars """

from odbinfo.pure.datatype import Token
from odbinfo.pure.dependency.searchtabular import (search_deps_in_queries,
                                                   search_tables_in_keys)


def test_search_deps_in_queries_match(table_plant, embedded_query):
    """match"""
    embedded_query.table_tokens = [Token('"plant"', 0, 0, False)]
    search_deps_in_queries([table_plant], [embedded_query])
    assert embedded_query.table_tokens[0].link == table_plant.identifier


def test_search_deps_in_queries_non_match(table_family, embedded_query):
    """non match"""
    embedded_query.table_tokens = [Token('"plant"', 0, 0, False)]
    search_deps_in_queries([table_family], [embedded_query])
    assert embedded_query.table_tokens[0].link is None


def test_search_tables_in_keys_match(table_plant, table_family):
    """match"""
    search_tables_in_keys([table_plant, table_family], [table_plant.keys[0]])
    assert table_plant.keys[0].link == table_family.identifier
