from fastapi.testclient import TestClient

from main import api

client = TestClient(api)


def path(action=None):
    prefix = "/v1/teams/"
    if action is not None:
        return prefix + action
    else:
        return prefix


def test_teams_get():
    response = client.get(path())
    assert response.status_code == 200


def test_teams_crud():
    # CREATE a team.
    response = client.post(path(), json={"name": "Test Team",})
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == "Test Team"
    team_id = content["id"]
    assert team_id != ""

    # TODO put

    # GET the new team.
    response = client.get(path(team_id))
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == "Test Team"

    # DELETE the team.
    response = client.delete(path(team_id))
    assert response.status_code == 204
