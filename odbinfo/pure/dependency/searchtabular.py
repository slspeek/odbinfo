" search dependencies in tabular objects "
from typing import Iterable, Sequence

from odbinfo.pure.datatype import EmbeddedQuery, Key, Table, Tabular, Token
from odbinfo.pure.dependency.util import link_token

#
# Queries, Tables, Views in Queries
#


def search_deps_in_queries(tabular_seq: Sequence[Tabular],
                           queries: Iterable[EmbeddedQuery]) -> None:
    " find uses of `tabulars` in `queries` "
    def find_tabulars_in_query(query: EmbeddedQuery) -> None:
        " find tabular uses in `query` "
        def find_tabular_in_query(tabular: Tabular) -> None:
            def find_tabular_in_token(token: Token) -> None:
                if tabular.users_match(token.text[1:-1]):
                    link_token(token, tabular)
            for token in query.table_tokens:
                find_tabular_in_token(token)
        for tabular in tabular_seq:
            find_tabular_in_query(tabular)
    for query in queries:
        find_tabulars_in_query(query)

#
# Tables in Tables
#


def search_tables_in_tables(tables: Sequence[Table]) -> None:
    " search for foreign key references amoung tables "
    def search_in_one_table(atable: Table) -> None:

        def search_one_key(key: Key) -> None:

            def match_table(othertable: Table) -> None:
                if othertable.users_match(key.referenced_table):
                    key.link = othertable.identifier
            for obj in tables:
                match_table(obj)
        for key in atable.keys:
            search_one_key(key)
    for table in tables:
        search_in_one_table(table)
