""" Core module """
import os
import time
from urllib.parse import urlparse

from odbinfo.oo.reader import read_metadata
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.writer import make_site


def generate_report(oodocument, config=get_configuration()):
    """ Make report """
    docpath = urlparse(oodocument.URL).path
    name, _ = os.path.splitext(os.path.basename(docpath))
    config.name = name
    if not config.general.output_dir:
        config.general.output_dir = \
            os.path.join(os.path.dirname(docpath), ".odbinfo")

    start_time = time.time()
    metadata = read_metadata(oodocument.DataSource, docpath)
    end_time = time.time()
    print("Read metadata: {}".format(end_time-start_time))

    start_time = time.time()
    process_metadata(metadata, config)
    end_time = time.time()
    print("Processing: {}".format(end_time-start_time))

    start_time = time.time()
    result = make_site(config.general.output_dir, name, metadata)
    end_time = time.time()
    print("Writing: {}".format(end_time-start_time))
    return result
