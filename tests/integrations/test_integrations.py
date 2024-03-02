import logging
import os
from pathlib import Path

import pytest
import toml
from fastapi.testclient import TestClient
from pyconarr.main import app as pyconarr
from tests.load_test_config import inputs, responses

my_version = toml.load(Path(os.getcwd()) / "pyproject.toml")["tool"]["poetry"][
    "version"
]


client = TestClient(pyconarr)


@pytest.mark.integration
def test_post_login_user():
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_real_user.json"],
    )
    logging.info(response.json())
    assert response.status_code == 200
    assert not response.json()["User"]["Policy"]["IsAdministrator"]
    assert (
        response.json()["User"]["Name"]
        == responses["response_login_standard_real_user.json"]["User"]["Name"]
    )
