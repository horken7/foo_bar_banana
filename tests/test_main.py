import pytest
from fastapi.testclient import TestClient

from src.foo_bar_banana.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.json().get("message", "")
