"""test for config module"""
import logging
import pathlib

from odbinfo.pure.datatype import config


def test_site_path(configuration):
    configuration.general.output_dir = "/tmp"
    assert configuration.site_path == pathlib.Path("/tmp/test_config")


def test_set_configuration_defaults_already_set(configuration):
    configuration.general.output_dir = "/tmp"
    configuration.textdocuments.search_locations = []
    configuration.textdocuments.db_registration_id = "foo"
    config.set_configuration_defaults(configuration,
                                      pathlib.Path("/var/testdb.odb"))
    assert configuration.general.output_dir == "/tmp"
    assert configuration.textdocuments.search_locations == []
    assert configuration.textdocuments.db_registration_id == "foo"


def test_set_configuration_defaults_nothing_set(configuration):
    config.set_configuration_defaults(configuration,
                                      pathlib.Path("/var/testdb.odb"))
    assert configuration.general.output_dir == "/var/.odbinfo"
    assert configuration.textdocuments.search_locations == ["/var"]
    assert configuration.textdocuments.db_registration_id == "testdb"


def test_get_configuration_non_existent(caplog, tmpdir):
    caplog.set_level(logging.INFO)
    config_path = pathlib.Path(tmpdir / "config.yml")
    config.get_configuration(config_path=config_path)
    assert caplog.records[
        0].message == f"  No config found at {str(config_path)}"
    assert caplog.records[
        1].message == f"  Wrote default configuration file at {str(config_path)}"
