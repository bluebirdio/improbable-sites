import pytest

from .crud import *

test_data = {"name": "Test Application", "description": "Test App Description"}


def path(action=""):
    prefix = "/v1/applications/"
    return prefix + action


@pytest.fixture(scope="session")
def test_application(client, test_team):
    # Does the test app already exist?
    response = client.get(path("test-application"))
    if response.status_code == 200:
        return response.json()

    # Test with No team value: should fail.
    response = client.post(path(), json=test_data)
    assert response.status_code == 422

    # Test with a valid team_id
    test_data["team_id"] = test_team["id"]
    response = client.post(path(), json=test_data)
    assert response.status_code == 201
    app = response.json()

    # Creating a duplicate app should fail.
    response = client.post(path(), json=test_data)
    assert response.status_code == 409

    return app


def test_application_delete(client, test_application):
    path_delete(client, path(test_application["id"]))
