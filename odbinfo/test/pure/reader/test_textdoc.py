" test reading odt and ott files "
import pytest

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.reader.textdoc import _text_documents, read_text_documents
from odbinfo.test.resource import DEFAULT_TESTDB


@pytest.mark.slow
def test_text_document(shared_datadir):
    " find odts "
    directory = (shared_datadir / DEFAULT_TESTDB).parent
    assert len(list(_text_documents(directory))) == 3


@pytest.mark.slow
def test_read_text_documents(shared_datadir):
    " find odts "
    directory = (shared_datadir / DEFAULT_TESTDB).parent

    print(read_text_documents(TextDocumentsConfig("testdb", [directory])))
