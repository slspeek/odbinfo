"test for graph module"
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.graph import visible_edges
from odbinfo.test.pure.fixtures import metadata_processed


def test_visible_edges(metadata_processed):
    "test default testdb"
    conf = get_configuration().graph
    visible_edges(metadata_processed, conf)


def test_visible_edges_no_collapse(metadata_processed):
    " no collapse_multiple_uses"
    conf = get_configuration().graph
    conf.collapse_multiple_uses = False
    conf.excludes.append("table")
    visible_edges(metadata_processed, conf)


def test_visible_edges_tables_excluded(metadata_processed):
    "tables excluded"
    conf = get_configuration().graph
    conf.excludes.append("table")
    visible_edges(metadata_processed, conf)
