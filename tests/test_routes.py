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


# def test_create_message():
#     """
#     Test POST /messages endpoint.
#
#     :return: None
#     """
#     # Create a test message
#     payload = {"dialogue_id": "1b40520b-05d6-419c-a136-1b5b72e9a3e5", "content": "Test message"}
#     response = client.post("/messages", json=payload)
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, dict)
#     assert "id" in data
#     assert "content" in data
#     assert "sender_type" in data
#     assert data["sender_type"] == "bot"
