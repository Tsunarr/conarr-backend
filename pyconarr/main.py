import pkg_resources
import toml
from fastapi import FastAPI
from pydantic import BaseModel

description = """
    API for Conarr, a containerized application for managing and organizing your media collection.

    Conarr allows you to manage sonarr, radarr, prowlarr, jellyseerr from a single interface. It is designed to be run in a containerized environment, and is built using FastAPI, Vue.js, and Docker.

    It also allow you to share some features to your jellyfin server without giving admin rights to your arr apps.
"""

openapi_tags_metadata = [{"name": "versions", "description": "API versions"}]

try:
    my_version = pkg_resources.get_distribution("conarr-backend").version
except pkg_resources.DistributionNotFound:
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


class Health(BaseModel):
    version: str


app = FastAPI(
    title="Conarr",
    description=description,
    summary="Conarr API",
    version=my_version,
    openapi_tags=openapi_tags_metadata,
    license_info={
        "name": "GPL v3",
        "identifier": "GPL-3.0-or-later",
    },
)


@app.get("/", tags=["versions"])
@app.get("/version", tags=["versions"])
@app.get("/health", tags=["versions"])
async def show_version() -> Health:
    return Health(version=my_version)
