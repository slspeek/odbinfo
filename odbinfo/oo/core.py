""" Core module """
import os
from urllib.parse import urlparse

from odbinfo.oo.reader import read_metadata
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.util import timed
from odbinfo.pure.writer import make_site


@timed("Generate report")
def generate_report(oodocument, config=get_configuration()):
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
