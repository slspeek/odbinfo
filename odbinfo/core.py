""" Core module """
import os
import shutil
from urllib.parse import urlparse
from odbinfo.writer import make_site
from odbinfo.reader import read_metadata


def generate_report(oodocument):
    """ Make report """
    docurl = oodocument.URL
    docpath = urlparse(docurl).path
    docdir = os.path.dirname(docpath)
    name, _ = os.path.splitext(os.path.basename(docpath))
    workingdir = os.path.join(docdir, ".odbinfo")
    reportdir = os.path.join(workingdir, name)
    if os.path.isdir(reportdir) and os.path.exists(reportdir):
        shutil.rmtree(reportdir)
        shutil.rmtree(f"{reportdir}-local")
    metadata = read_metadata(oodocument.DataSource, docpath)
    return make_site(workingdir, name, metadata)
