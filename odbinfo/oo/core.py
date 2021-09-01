""" Core module """
import os
from pathlib import Path
from urllib.parse import urlparse

import yaml

from odbinfo.oo.reader import read_metadata
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.util import timed
from odbinfo.pure.writer import make_site


def default_config_path():
    " returns the default location of the configuration file "
    return Path.home() / ".odbinfo" / "config.yaml"


def read_configuration(config_path=default_config_path()):
    " reads configuration from `config_path` if exits "\
        " otherwise a default configuration is written in `config_path`"
    if not config_path.exists():
        if not config_path.parent.exists():
            config_path.parent.mkdir()
        config = get_configuration()
        with config_path.open(mode='w') as output_file:
            yaml.dump(config, output_file)
        return config
    with config_path.open() as file:
        return yaml.load(file, Loader=yaml.Loader)


@timed("Generate report")
def generate_report(oodocument, config=read_configuration()):
    """ Make report """
    docpath = urlparse(oodocument.URL).path
    name, _ = os.path.splitext(os.path.basename(docpath))
    config.name = name
    if not config.general.output_dir:
        config.general.output_dir = \
            os.path.join(os.path.dirname(docpath), ".odbinfo")

    metadata = read_metadata(oodocument.DataSource, docpath)

    process_metadata(metadata, config)

    result = make_site(config, metadata)
    return result
