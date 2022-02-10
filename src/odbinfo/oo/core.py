""" Core module """

import logging

from odbinfo.oo import ooutil
from odbinfo.oo.dialog import create_logging_dialog
from odbinfo.oo.reader import read_metadata
from odbinfo.pure.builder import build
from odbinfo.pure.datatype.config import (get_configuration,
                                          set_configuration_defaults)
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.util import timed
from odbinfo.pure.writer import write_site


@timed("Generate report")
def _generate_report(oodocument, config=None):
    if not config:
        config = get_configuration()

    odbpath = ooutil.document_path(oodocument)

    set_configuration_defaults(config, odbpath)

    metadata = read_metadata(config, oodocument.DataSource, odbpath)

    process_metadata(config, metadata)

    write_site(config, metadata)

    build(config.site_path)


def generate_report(oodocument, config=None, gui=False, ctx=None):
    """ Make report """
    logging.basicConfig(level=logging.INFO)
    if gui:
        dialog = create_logging_dialog(
            _generate_report, oodocument, config, ctx=ctx)
        dialog.execute()
    else:
        _generate_report(oodocument, config)
