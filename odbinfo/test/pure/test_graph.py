"test for graph module"
from odbinfo.pure.datatype import Control
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.graph import generate_main_graph, is_visible, visible_edges
from odbinfo.test.pure.fixtures import metadata_processed


def test_visible_edges(metadata_processed):
    "test default testdb"
    conf = get_configuration().graph
    visible_edges(metadata_processed, conf)


def test_is_visible():
    "test relevant_controls=False "
    node = Control("control1", "c1", None, False, True,
                   "Label", "otherControl", "text", [])
    conf = get_configuration().graph
    conf.relevant_controls = False
    assert is_visible(conf, node)


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


def test_generate_main_graph(metadata_processed):
    "run generate_main_graph with relevant_controls off for coverage"
    conf = get_configuration()
    conf.name = "test_generate_main_graph"
    conf.graph.relevant_controls = False
    generate_main_graph(metadata_processed, conf)
