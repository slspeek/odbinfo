""" Core module """
import os
import shutil
from urllib.parse import urlparse
from odbinfo.writer import make_site
from odbinfo.reader import read_metadata
from odbinfo.parser.basic import get_basic_tokens, scan_basic
from odbinfo.datatype import Library, Module, Callable


def _process_library(library: Library):
    def parse_module(module: Module):
        # print("parsing: " + module.source)
        module.callables =\
            scan_basic(module.source, library.name, module.name)

    list(map(parse_module, library.modules))


def _tokenize_library(library: Library):
    def tokenize_module(module: Module):
        module.tokens =\
            get_basic_tokens(module.source)

        def tokenize_callable(acallable: Callable):
            acallable.tokens =\
                get_basic_tokens(acallable.source)
        list(map(tokenize_callable, module.callables))
    list(map(tokenize_module, library.modules))


def _process_libraries(libraries: [Library]):
    list(map(_process_library, libraries))
    list(map(_tokenize_library, libraries))


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
