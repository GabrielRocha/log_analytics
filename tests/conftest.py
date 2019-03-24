import os

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def dir_file():
    return os.path.dirname(os.path.abspath(__file__))
