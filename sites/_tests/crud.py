import pytest


def default_items():
    return {
        "teams": {
            "id": "test-team",
            "name": "Test Team",
            "description": "Test team description",
        },
        "stacks": {
            "id": "test-stack",
            "name": "Test Stack",
            "description": "Test stack description",
        },
        "applications": {
            "id": "test-application",
            "team_id": "test-team",
            "name": "Test Application",
            "description": "Test App Description",
        },
        "instances": {
            "name": "Test instance",
            "application_id": "test-application",
            "instance_group": "default",
            "stack_id": "test-stack",
            "environment": "production",
            "url": "http://example.com",
        },
    }


def path_delete(client, path):
    response = client.delete(path)
    assert response.status_code == 204

    response = client.get(path)
    assert response.status_code == 404


@pytest.fixture(scope="session")
def test_stack(client):
    path = "/v1/stacks/"
    stack = default_items()["stacks"]
    stack_path = path + stack["id"]

    response = client.get(path)
    if response.status_code == 200:
        return response.json()

    response = client.post(path, json=stack)
    assert response.status_code == 200
    return response.json()
