"""
This file contains the tests for the REST API routes.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_characters():
    """
    Test GET /characters endpoint.

    :return: None
    """
    response = client.get("/characters")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "characters" in data
    assert isinstance(data["characters"], list)
