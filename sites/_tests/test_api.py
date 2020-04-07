import pytest

from .crud import *


def format_default_items():
    """
    Re-structure the default_items dictionary result as a list appropriate for paramaterizing.
    :return: list
    """
    formatted = []
    for path, item in default_items().items():
        formatted.append((path, item))
    return formatted


@pytest.mark.parametrize("path,item", format_default_items())
def test_api_list(client, path, item):
    path = "/v1/" + path
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.usefixtures("test_team", "test_application", "test_stack")
@pytest.mark.parametrize("path,item", format_default_items())
def test_default_create(client, path, item):
    path = "/v1/" + path + "/"

    # CREATE
    response = client.post(path, json=item)
    assert response.status_code in [201, 409]
    item = response.json()
    print(item)
    item_path = path + item["id"]

    # GET
    response = client.get(item_path)
    assert response.status_code == 200

    # DELETE
    response = client.delete(item_path)
    assert response.status_code == 204

    # confirm DELETE
    response = client.get(item_path)
    assert response.status_code == 404
