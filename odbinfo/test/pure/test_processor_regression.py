" Tests for the processor "
import dataclasses
import os
import pickle

from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.processor import process_metadata
from odbinfo.test.pure.fixtures import empty_metadata_loader, metadata_loader


def test_processor_regression(metadata_loader, data_regression, file_regression,
                              benchmark):
    " regression test "
    # print("All objects count:", len(metadata.all_objects()))
    process_and_check(metadata_loader, "metadata-processed",
                      data_regression, file_regression, benchmark)


def test_processor_regression_empty(empty_metadata_loader, data_regression,
                                    file_regression, benchmark):
    " regression test on empty database"
    process_and_check(empty_metadata_loader, "empty-metadata-processed",
                      data_regression, file_regression, benchmark)


def process_and_check(unprocessed, filename, data_regression,
                      file_regression, benchmark):
    " do processing and check"
    def setup():
        metadata = unprocessed()
        config = get_configuration()
        config.name, _ = os.path.splitext(os.path.basename(metadata.name))
        print("NAME:", config.name)
        return (metadata, config), {}
    processed = benchmark.pedantic(process_metadata, setup=setup)
    # data_regression.check(unprocessed)
    processed.graphs = []
    file_regression.check(pickle.dumps(processed), binary=True,
                          basename=filename, extension=".pickle")
    for obj in processed.all_objects():
        obj.parent = None
    data_regression.check(dataclasses.asdict(processed))
