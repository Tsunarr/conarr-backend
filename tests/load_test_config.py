import json
import os
from pathlib import Path

import toml
from fastapi.testclient import TestClient
from pyconarr.main import app as pyconarr

responses = {}

for filename in os.listdir("tests/responses"):
    with open(os.path.join("tests/responses", filename)) as f:
        responses[filename] = json.loads(f.read())

inputs = {}

for filename in os.listdir("tests/inputs"):
    with open(os.path.join("tests/inputs", filename)) as f:
        inputs[filename] = json.loads(f.read())

my_version = toml.load(Path(os.getcwd()) / "pyproject.toml")["tool"]["poetry"][
    "version"
]

client = TestClient(pyconarr)
