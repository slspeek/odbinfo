"directory_regression test"
from pathlib import Path
from unittest.mock import patch

import pytest

from odbinfo.pure import writer
from odbinfo.pure.writer import convert_local
from odbinfo.test.regression import directory_regression


@pytest.mark.slow
def test_run_check(directory_regression, shared_datadir):
    with patch.object(writer, 'find_free_port', return_value=1313):
        convert_local(Path(shared_datadir)
                      / "fixtures" / "convert_local_input")
        directory_regression.check(
            Path(shared_datadir) / "fixtures" / "convert_local_input-local",
        )
