import os
from importlib import metadata
from pathlib import Path

import toml
import yaml


def get_version():
    try:
        my_version = metadata.version("pyconarr")
    except metadata.PackageNotFoundError:
        my_version = toml.load(Path(os.getcwd()) / "pyproject.toml")["tool"]["poetry"][
            "version"
        ]
    return my_version


with open("config/pyconarr.yml", "r") as f:
    config = yaml.safe_load(f)
