""" Core module """

import logging

from odbinfo.oo import ooutil
from odbinfo.oo.dialog import create_logging_dialog
from odbinfo.oo.reader import read_metadata
from odbinfo.pure.builder import build
from odbinfo.pure.datatype.config import (Configuration, get_configuration,
                                          set_configuration_defaults)
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.util import timed
from odbinfo.pure.writer import write_site


@timed("Generate report")
def generate_report(oodocument,
                    config: Configuration = None,
                    open_browser: bool = False):
    """ Generates the report of the staroffice `oodocument`, using configuration `config`.

        1. It loads the configuration and sets defaults in it.
        2. Reads the metatdata.
        3. Processes the metadata, this includes a dependency search.
        4. Write the result to disk for further rendering by gohugo.
        5. Invokes hugo and opens a browser on the result.
    """
    # noinspection PyBroadException
    try:
        if not config:
            config = get_configuration()

        odbpath = ooutil.document_path(oodocument)

        set_configuration_defaults(config, odbpath)

        metadata = read_metadata(config, oodocument.DataSource, odbpath)

        process_metadata(config, metadata)

        write_site(config, metadata)

        build(config.site_path, open_browser)
    except Exception:  # pylint:disable=broad-except
        logging.exception("Unexpected exception")


def generate_report_ui(oodocument,
                       config: Configuration = None,
                       gui: bool = False,
                       open_browser: bool = False,
                       ctx=None):
    """ Generates a report of the staroffice document `oodocument` using configuration `config`.
        If `gui` is False it runs headless, else it shows a dialog.
        If `openbrowser` is True it opens a browser on the generated report.
        `ctx` needs to be a staroffice context, and is only needed if `gui`=True.
        """
    logging.basicConfig(level=logging.INFO)
    if gui:
        dialog = create_logging_dialog(generate_report,
                                       oodocument,
                                       config,
                                       open_browser,
                                       ctx=ctx)
        dialog.execute()
    else:
        generate_report(oodocument, config, open_browser)
