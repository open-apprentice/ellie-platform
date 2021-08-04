import pytest

from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_create_user(client):
    payload = {
        "first_name": "tim",
        "last_name": "ferriss",
        "is_admin": True,
        "user_email": "user@example.com",
    }
    response = client.post("/user", json=payload)
    assert response.status_code == 201
    #{'success': True, 'created_id': 1}
    #assert response.json() == expected
