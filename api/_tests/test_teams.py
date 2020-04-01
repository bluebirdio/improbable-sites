from fastapi.testclient import TestClient

from main import api

client = TestClient(api)


def path(action=""):
    prefix = "/v1/teams/"
    return prefix + action


def test_teams_get():
    response = client.get(path())
    assert response.status_code == 200


def test_teams_crud():
    # CREATE a team.
    response = client.post(path(), json={"name": "Test Team",})
    assert response.status_code == 201

    content = response.json()
    assert content["name"] == "Test Team"
    team_id = content["id"]
    assert team_id != ""

    # CREATE duplicate team: should fail with 422.
    response = client.post(path(), json={"id": team_id, "name": "Test Team",})
    assert response.status_code == 422

    # GET the new team.
    response = client.get(path(team_id))
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == "Test Team"

    # UPDATE team.
    response = client.put(
        path(team_id), json={"name": "Test Team", "description": "DESC"}
    )
    assert response.status_code == 200

    content = response.json()
    assert content["description"] == "DESC"

    # DELETE the team.
    response = client.delete(path(team_id))
    assert response.status_code == 204

    response = client.get(path(team_id))
    assert response.status_code == 404
