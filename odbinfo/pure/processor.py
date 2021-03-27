""" Core module """
from odbinfo.pure.datatype import Callable, Library, Module
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic


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
