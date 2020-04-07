import pytest

from .crud import *


def path(action=""):
    prefix = "/v1/applications/"
    return prefix + action


@pytest.fixture(scope="session")
def test_application(client, test_team):
    application = default_items()["applications"]
    # Does the test app already exist?
    response = client.get(path("test-application"))
    if response.status_code == 200:
        return response.json()

    # Test with No team value: should fail.
    missing_team = application
    application.pop("team_id")
    response = client.post(path(), json=application)
    assert response.status_code == 422

    # Test with a valid team_id
    application["team_id"] = test_team["id"]
    response = client.post(path(), json=application)
    assert response.status_code == 201
    app = response.json()

    return app
