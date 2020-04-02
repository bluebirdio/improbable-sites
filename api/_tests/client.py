from fastapi.testclient import TestClient

from main import api

client = TestClient(api)
