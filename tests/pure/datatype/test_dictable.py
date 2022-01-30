""" tests for dictable module """
from odbinfo.pure.datatype import config
from odbinfo.pure.datatype.base import Identifier


def test_from_dict_text():
    textdocconf = config.TextDocumentsConfig(
        **{"db_registration_id": "db_id", "search_locations": ["searchpath1"]})
    assert isinstance(textdocconf, config.TextDocumentsConfig)
    assert textdocconf.db_registration_id == "db_id"
    assert textdocconf.search_locations == ["searchpath1"]


def test_from_dict_general():
    genconf = config.GeneralConfig(
        **{"output_dir": "out", "base_url": "www.odbinfo.org"})
    assert isinstance(genconf, config.GeneralConfig)
    assert genconf.output_dir == "out"
    assert genconf.base_url == "www.odbinfo.org"


def test_to_dict_identitifier_no_bookmark():
    identifier = Identifier("foo", "bar", None)
    assert identifier.to_dict() == {'content_type': "foo", 'local_id': "bar"}


def test_to_dict_identitifier():
    identifier = Identifier("foo", "bar", "barbar")
    assert identifier.to_dict() == {'content_type': "foo",
                                    'local_id': "bar",
                                    "bookmark": "barbar"}


def test_node_to_dict(table_plant, foreignkey_family):
    assert table_plant.to_dict()["keys"][0] == foreignkey_family.to_dict()
