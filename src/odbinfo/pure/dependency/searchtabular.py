""" search dependencies in tabular objects """
from typing import Sequence

from odbinfo.pure.datatype import Key, QueryBase, Table, Tabular
from odbinfo.pure.dependency.util import product_search


#
# Queries, Tables, Views in Queries
#


def search_deps_in_queries(tabular_seq: Sequence[Tabular],
                           queries: Sequence[QueryBase]) -> None:
    """ find uses of `tabulars` in `queries` """
    product_search(sources=queries, targets=tabular_seq)


#
# Tables in Keys
#


def search_tables_in_keys(tables: Sequence[Table], keys: Sequence[Key]) -> None:
    """ search for foreign key references amoung tables """
    product_search(sources=keys, targets=tables)
