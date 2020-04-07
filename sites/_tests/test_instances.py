import pytest

from .crud import *


@pytest.fixture(scope="session")
def test_instance(client, test_application, test_stack):
    instance = default_items()["instance"]

    response = client.post(path(), json=instance)
    assert response.status_code == 201

    return instance


def test_duplicate_instance(client, test_application, test_stack):
    pass


def path(action=""):
    prefix = "/v1/instances/"
    return prefix + action
