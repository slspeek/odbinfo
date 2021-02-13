""" Core module """
import os
import shutil
from urllib.parse import urlparse
from odbinfo.writer import make_site
from odbinfo.reader import read_metadata
from odbinfo.parser.basic import parse
from odbinfo.datatype import Library, Module


def _process_library(library: Library):
    def parse_module(module: Module):
        # print("parsing: " + module.source)
        module.callables =\
            parse(module.source)

    list(map(parse_module, library.modules))


def _process_libraries(libraries: [Library]):
    list(map(_process_library, libraries))


def process_metadata(metadata):
    " preprocessing of the data before it is send to hugo "
    _process_libraries(metadata.libraries)


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
    process_metadata(metadata)
    return make_site(workingdir, name, metadata)
