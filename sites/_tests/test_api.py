import pytest


@pytest.mark.parametrize(
    "path",
    [
        "/v1/applications",
        "/v1/instances",
        "/v1/repositories",
        "/v1/roles",
        "/v1/stacks",
        "/v1/teams",
        "/v1/users",
    ],
)
def test_api_list(client, path):
    response = client.get(path)
    assert response.status_code == 200
