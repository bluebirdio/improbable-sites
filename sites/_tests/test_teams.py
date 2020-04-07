import pytest

from .crud import *


@pytest.fixture(scope="session")
def test_team(client):
    default_team = default_items()["teams"]
    # Does the test team already exist?
    response = client.get(path("test-team"))
    if response.status_code == 200:
        return response.json()

    response = client.post(path(), json=default_team)
    assert response.status_code == 201
    return response.json()


def path(action=""):
    prefix = "/v1/teams/"
    return prefix + action


def test_team_update(client, test_team):
    # UPDATE team.
    response = client.put(
        path(test_team["id"]), json={"name": "Test Team", "description": "DESC"}
    )
    assert response.status_code == 200

    content = response.json()
    assert content["description"] == "DESC"
