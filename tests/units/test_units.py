import os
from pathlib import Path

import pytest
import toml
from pyconarr.libs.config import get_version


@pytest.mark.unit
def test_config():
    version = get_version()
    assert (
        version
        == toml.load(Path(os.getcwd()) / "pyproject.toml")["tool"]["poetry"]["version"]
    )
