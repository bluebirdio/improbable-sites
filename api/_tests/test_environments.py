import pytest
from api.environments.values import default_environments


def path(action=""):
    prefix = "/v1/environments/"
    return prefix + action


@pytest.fixture(scope="session")
def test_environments(client):
    environments = []
    for env in default_environments():
        response = client.post(path(), env)
        assert response.status_code == 201
        environments.append(response.json())
    return environments

