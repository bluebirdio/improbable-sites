import pytest


@pytest.fixture(scope="session")
def test_team(client):
    # Does the test team already exist?
    response = client.get(path("test-team"))
    if response.status_code == 200:
        return response.json()

    test_data = {"name": "Test Team", "description": "Test team description"}
    response = client.post(path(), json=test_data)
    assert response.status_code == 201
    test_team = response.json()

    # Test duplicate create: should fail.
    response = client.post(path(), json=test_data)
    assert response.status_code == 422

    return test_team


def path(action=""):
    prefix = "/v1/teams/"
    return prefix + action


def test_teams_list(client):
    response = client.get(path())
    assert response.status_code == 200


def test_team_get(client, test_team):
    response = client.get(path(test_team["id"]))
    assert response.status_code == 200


def test_team_update(client, test_team):
    # UPDATE team.
    response = client.put(
        path(test_team["id"]), json={"name": "Test Team", "description": "DESC"}
    )
    assert response.status_code == 200

    content = response.json()
    assert content["description"] == "DESC"


def test_team_delete(client, test_team):
    team_id = test_team["id"]

    response = client.delete(path(team_id))
    assert response.status_code == 204

    response = client.get(path(team_id))
    assert response.status_code == 404
