import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.db import get_db, Base
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """
    https://fastapi.tiangolo.com/es/advanced/testing-database/
    - but had to move create_all to here!
    """
    try:
        Base.metadata.create_all(bind=engine)
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def database_override():
    app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


def test_user_crud(client):
    payload = {
        "first_name": "tim",
        "last_name": "ferriss",
        "is_admin": True,
        "user_email": "user@example.com",
    }
    response = client.post("/user", json=payload)
    assert response.status_code == 201, response.text
    expected = {"success": True, "created_id": 1}
    assert response.json() == expected
    response = client.get("/user/1")
    assert response.status_code == 200, response.text
    data = response.json()
    expected = {
        "last_name": "ferriss",
        "first_name": "tim",
        "user_email": "user@example.com",
        "id": 1,
        "is_admin": True,
    }
    assert data == expected
    response = client.delete("/user/1")
    assert response.status_code == 204, response.text
    assert response.json() == {"success": True}
