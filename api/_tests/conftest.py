import pytest
from fastapi.testclient import TestClient
from main import api
from api.migrate import *

from .test_teams import test_team
from .test_apps import test_app
from .test_environments import test_environments


@pytest.fixture(scope="session")
def client(test_db):
    client = TestClient(api)
    return client


@pytest.fixture(scope="session")
def test_db():
    create_all()

    yield

    drop_all()


