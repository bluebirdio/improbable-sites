import pytest
from fastapi.testclient import TestClient

from api.migrate import *
from main import api

from .test_applications import test_application
from .test_teams import test_team


@pytest.fixture(scope="session")
def client(test_db):
    client = TestClient(api)
    return client


@pytest.fixture(scope="session")
def test_db():
    create_all()

    yield
