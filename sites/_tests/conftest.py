import pytest
from fastapi.testclient import TestClient

from main import api
from sites.migrate import *

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
