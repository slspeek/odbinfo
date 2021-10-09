" test dependency search in tabulars "
import unittest

from odbinfo.pure.datatype import Token, EmbeddedQuery
from odbinfo.pure.dependency.searchtabular import (search_deps_in_queries,
                                                   search_tables_in_tables)
from odbinfo.test.pure.datatype import factory


class InQueries(unittest.TestCase):
    "search_deps_in_queries"

    def setUp(self):
        self.plant = factory.table_plant()
        self.query: EmbeddedQuery = factory.embedded_query()
        self.query.table_tokens = [Token('"plant"', 0, 0, False)]

    def test_match(self):
        "match"
        search_deps_in_queries([self.plant], [self.query])
        assert self.query.table_tokens[0].link == self.plant.identifier

    def test_non_match(self):
        "non match"
        family = factory.table_family()
        search_deps_in_queries([family], [self.query])
        assert self.query.table_tokens[0].link is None


class TablesInTables(unittest.TestCase):
    "search_tables_in_tables"

    def setUp(self):
        self.plant = factory.table_plant()
        self.family = factory.table_family()

    def test_match(self):
        "match"
        search_tables_in_tables([self.plant, self.family])
        assert self.plant.keys[0].link == self.family.identifier
