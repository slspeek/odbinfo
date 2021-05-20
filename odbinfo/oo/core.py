""" Core module """
import os
from urllib.parse import urlparse

from odbinfo.oo.reader import read_metadata
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.writer import make_site


def generate_report(oodocument, output_dir=None):
    """ Make report """
    docpath = urlparse(oodocument.URL).path
    name, _ = os.path.splitext(os.path.basename(docpath))
    if not output_dir:
        output_dir = os.path.join(os.path.dirname(docpath), ".odbinfo")

    metadata = read_metadata(oodocument.DataSource, docpath)
    process_metadata(metadata)
    return make_site(output_dir, name, metadata)
