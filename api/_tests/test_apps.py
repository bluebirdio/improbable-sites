import pytest

test_data = {"name": "Test Application", "description": "Test App Description"}


def path(action=""):
    prefix = "/v1/apps/"
    return prefix + action


@pytest.fixture(scope="session")
def test_app(client, test_team):
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
    assert response.status_code == 422

    return app


def test_apps_list(client):
    response = client.get(path())
    assert response.status_code == 200


def test_app_delete(client, test_app):
    app_id = test_app["id"]
    response = client.delete(path(app_id))
    assert response.status_code == 204

    response = client.get(path(app_id))
    assert response.status_code == 404
