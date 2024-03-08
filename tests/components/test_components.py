import logging

import pytest
import requests
from pyconarr.main import config
from tests.load_test_config import client, inputs, my_version, responses


def call_version_endpoint(requests_mock, endpoint):
    requests_mock.get(
        config["jellyfin"]["url"] + "/System/Info/Public",
        json=responses["response_system_info_public.json"],
    )
    response = client.get(endpoint)
    logging.info(response.json())
    valid_json = {
        "jellyfin": {
            "version": responses["response_system_info_public.json"]["Version"]
        },
        "conarr": {"version": my_version},
    }
    assert response.status_code == 200
    assert response.json() == valid_json


@pytest.mark.component
def test_get_root(requests_mock):
    call_version_endpoint(requests_mock, "/")


@pytest.mark.component
def test_get_version(requests_mock):
    call_version_endpoint(requests_mock, "/version")


@pytest.mark.component
def test_post_login_admin(requests_mock):
    requests_mock.post(
        config["jellyfin"]["url"] + "/Users/AuthenticateByName",
        json=responses["response_login_admin_user.json"],
    )
    requests_mock.get(
        config["jellyfin"]["url"]
        + "/Users/"
        + inputs["input_login_admin.json"]["Username"],
        status_code=200,
    )

    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_admin.json"],
    )
    logging.info(response.json())
    assert response.status_code == 200
    assert response.json() == responses["response_login_admin_user.json"]
    assert response.json()["User"]["Policy"]["IsAdministrator"]
    assert (
        response.json()["User"]["Name"]
        == responses["response_login_admin_user.json"]["User"]["Name"]
    )


@pytest.mark.component
def test_post_login_user(requests_mock):
    requests_mock.post(
        config["jellyfin"]["url"] + "/Users/AuthenticateByName",
        json=responses["response_login_standard_user.json"],
    )
    requests_mock.get(
        config["jellyfin"]["url"]
        + "/Users/"
        + inputs["input_login_user.json"]["Username"],
        status_code=200,
    )
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_user.json"],
    )
    logging.info(response.json())
    assert response.status_code == 200
    assert response.json() == responses["response_login_standard_user.json"]
    assert not response.json()["User"]["Policy"]["IsAdministrator"]
    assert (
        response.json()["User"]["Name"]
        == responses["response_login_standard_user.json"]["User"]["Name"]
    )


@pytest.mark.component
def test_error_timeout_post_login_user(requests_mock):
    requests_mock.post(
        config["jellyfin"]["url"] + "/Users/AuthenticateByName",
        exc=requests.exceptions.ReadTimeout,
    )
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_user.json"],
    )
    logging.info(response.json())
    assert response.status_code == 502
    assert response.json() == {"detail": "Failed to contact jellyfin server"}


@pytest.mark.component
def test_error_timeout_post_login_user_valid(requests_mock):
    requests_mock.post(
        config["jellyfin"]["url"] + "/Users/AuthenticateByName",
        status_code=401,
    )
    requests_mock.get(
        config["jellyfin"]["url"]
        + "/Users",
        exc=requests.exceptions.ReadTimeout,
    )
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_user.json"],
    )
    assert response.status_code == 502
    assert response.json() == {"detail": "Failed to contact jellyfin server"}


@pytest.mark.component
def test_error_wrong_password_post_login_user(requests_mock):
    requests_mock.post(
        config["jellyfin"]["url"] + "/Users/AuthenticateByName",
        status_code=401,
    )
    requests_mock.get(
        config["jellyfin"]["url"]
        + "/Users",
        status_code=200,
        json=responses["response_list_users.json"],
    )
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_user.json"],
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Login failed"}


@pytest.mark.component
def test_error_wrong_username_post_login_user(requests_mock):
    requests_mock.post(
        config["jellyfin"]["url"] + "/Users/AuthenticateByName",
        status_code=401,
    )
    requests_mock.get(
        config["jellyfin"]["url"]
        + "/Users",
        status_code=200,
        json=responses["response_list_users.json"],
    )
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_user.json"],
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Login failed"}


@pytest.mark.component
def test_error_not_implemented_post_login_user(requests_mock):
    requests_mock.post(
        config["jellyfin"]["url"] + "/Users/AuthenticateByName",
        status_code=418,
    )
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/json"},
        json=inputs["input_login_user.json"],
    )
    assert response.status_code == 502
    assert response.json() == {"detail": "Failed to contact jellyfin server"}
