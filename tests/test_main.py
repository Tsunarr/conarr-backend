import toml
from fastapi.testclient import TestClient
from pyconarr.main import app

try:
    # devcontainer location
    my_version = toml.load("/workspaces/conarr-backend/pyproject.toml")["tool"][
        "poetry"
    ]["version"]
except FileNotFoundError:
    # github action location
    my_version = toml.load(
        "/home/runner/work/conarr-backend/conarr-backend/pyproject.toml"
    )["tool"]["poetry"]["version"]

client = TestClient(app)


def test_read_version():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"version": my_version}
