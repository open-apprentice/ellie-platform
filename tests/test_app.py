import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.db import get_db, Base
from main import app
from schemas.users import CreateUser

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        Base.metadata.create_all(bind=engine)
        db = TestingSessionLocal()
        yield db
    finally:
        Base.metadata.drop_all(bind=engine)
        db.close()


@pytest.fixture(scope="session", autouse=True)
def database_override():
    app.dependency_overrides[get_db] = override_get_db


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
    print(response)
    breakpoint()
    assert response.status_code == 201
    expected = {"success": True, "created_id": 1}
    assert response.json() == expected


def test_create_course(client):
    pass
