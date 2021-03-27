"""" Test fixtures """
import pickle

from pytest import fixture

from odbinfo.test.resource import FIXTURE_DIR


def load_metadata():
    """ Returns Metadata object from the test fixture """
    with open(FIXTURE_DIR.format('metadata.pickle'), 'rb') as file:
        meta = pickle.load(file)
    return meta


@fixture(scope="session")
def metadata():
    """ Array of all objects from repository """
    yield load_metadata()
