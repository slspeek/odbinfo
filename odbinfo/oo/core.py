""" Core module """
import os
import shutil
from urllib.parse import urlparse

from odbinfo.oo.reader import read_metadata
from odbinfo.pure.processor import process_metadata
from odbinfo.pure.writer import make_site


def generate_report(oodocument, output_dir=None):
    """ Make report """
    docurl = oodocument.URL
    docpath = urlparse(docurl).path

    docdir = os.path.dirname(docpath)
    name, _ = os.path.splitext(os.path.basename(docpath))
    if not output_dir:
        output_dir = os.path.join(docdir, ".odbinfo")

    reportdir = os.path.join(output_dir, name)

    def rmtree(directory):
        if os.path.isdir(directory) and os.path.exists(directory):
            shutil.rmtree(directory)

    rmtree(reportdir)
    rmtree(f"{reportdir}-local")
    metadata = read_metadata(oodocument.DataSource, docpath)
    process_metadata(metadata)
    return make_site(output_dir, name, metadata)
