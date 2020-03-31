from fastapi.testclient import TestClient

from main import api

client = TestClient(api)


def test_get_teams():
    response = client.get("/teams")
    assert response.status_code == 200


def test_team_crud():
    # CREATE a team.
    response = client.post("/teams/", json={"name": "Test Team",})
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == "Test Team"
    team_id = content["id"]
    assert team_id != ""

    # TODO put

    # GET the new team.
    response = client.get("/teams/" + team_id)
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == "Test Team"

    # GET team locations
    response = client.get("/teams/" + team_id + "/locations")
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 0

    # CREATE a new team location
    response = client.post(
        "/teams/" + team_id + "/locations",
        json={
            "name": "Test Vendor",
            "url": "http://www.example.com/",
            "phone": "6125551212",
        },
    )

    # DELETE the team.
    response = client.delete("/teams/" + team_id)
    assert response.status_code == 204
