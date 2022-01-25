""" Core module """
from pathlib import Path

import yaml

from odbinfo.oo import ooutil
from odbinfo.oo.reader import read_metadata
from odbinfo.pure.builder import build
from odbinfo.pure.datatype.config import Configuration, get_configuration
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.util import timed
from odbinfo.pure.writer import write_site


def default_config_path() -> Path:
    """ returns the default location of the configuration file """
    return Path.home() / ".odbinfo" / "config.yaml"


def read_configuration(config_path: Path = default_config_path()):
    """ reads configuration from `config_path` if exits "\
        " otherwise a default configuration is written in `config_path`"""
    if not config_path.exists():
        if not config_path.parent.exists():
            config_path.parent.mkdir()
        config = get_configuration()
        with config_path.open(mode='w', encoding='utf-8') as output_file:
            yaml.dump(config, output_file)
        return config
    with config_path.open(encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.Loader)


def set_configuration_defaults(config: Configuration, odbpath: Path):
    """ sets sensible defaults """
    config.name = odbpath.stem
    if not config.general.output_dir:
        config.general.output_dir = str(odbpath.parent / ".odbinfo")
    if not config.textdocuments.db_registration_id:
        config.textdocuments.db_registration_id = config.name
    if config.textdocuments.search_locations is None:
        config.textdocuments.search_locations = [str(odbpath.parent)]


@timed("Generate report")
def generate_report(oodocument, config=None, gui=False):
    """ Make report """

    if not config:
        config = read_configuration()

    odbpath = ooutil.document_path(oodocument)

    set_configuration_defaults(config, odbpath)

    metadata = read_metadata(config, oodocument.DataSource, odbpath)

    process_metadata(config, metadata)

    write_site(config, metadata)

    build(config.site_path)

    if gui:
        # noinspection PyUnresolvedReferences
        # pylint:disable=import-outside-toplevel
        from apso_utils import msgbox
        msgbox("Hello")
