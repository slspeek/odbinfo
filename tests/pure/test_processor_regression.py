""" Tests for the processor """
import dataclasses
import pickle

import pytest

from odbinfo.pure.datatype.config import create_configuration
from odbinfo.pure.processor import process_metadata


@pytest.mark.slow
def test_processor_regression(metadata_loader, data_regression,
                              file_regression, benchmark):
    """ regression test """
    # print("All objects count:", len(metadata.all_objects()))
    process_and_check(metadata_loader, "metadata-processed", data_regression,
                      file_regression, benchmark)


@pytest.mark.slow
def test_processor_regression_empty(empty_metadata_loader, data_regression,
                                    file_regression, benchmark):
    """ regression test on empty database"""
    process_and_check(empty_metadata_loader, "empty-metadata-processed",
                      data_regression, file_regression, benchmark)


def process_and_check(unprocessed, filename, data_regression, file_regression,
                      benchmark):
    """ do processing and check"""

    def setup():
        metadata = unprocessed()
        config = create_configuration(metadata.name)
        return (config, metadata), {}

    processed = benchmark.pedantic(process_metadata, setup=setup)
    file_regression.check(pickle.dumps(processed),
                          binary=True,
                          basename=filename,
                          extension=".pickle")

    graph_txt = "No graph"
    if processed.graph:
        graph_txt = processed.graph.source

    file_regression.check(graph_txt,
                          binary=False,
                          basename=f"{filename}-graphs",
                          extension=".txt")

    processed.graph = None
    for obj in processed.all_objects():
        obj.parent = None
    data_regression.check(dataclasses.asdict(processed))
