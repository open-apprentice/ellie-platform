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
TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False, bind=engine)


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
    response = client.get("/user/1")
    assert response.status_code == 404, response.text


def test_course_crud(client):
    payload = {
        "course_name": "100 days of code",
        "is_draft": False,
        "is_published": True,
        "date_published": "2021-08-14",
        "last_updated": "2021-08-14",
        "author": "mike, julian and bob",
    }
    response = client.post("/course", json=payload)
    assert response.status_code == 201, response.text
    assert response.json() == {"success": True, "created_id": 1}
    response = client.get("/course/1")
    data = response.json()
    expected = {
        "is_draft": False,
        "date_published": "2021-08-14",
        "author": "mike, julian and bob",
        "is_published": True,
        "course_name": "100 days of code",
        "id": 1,
        "last_updated": "2021-08-14",
    }
    assert response.status_code == 200, response.text
    assert data == expected
    response = client.delete("/course/1")
    assert response.status_code == 204, response.text
    assert response.json() == {"success": True}
    response = client.get("/course/1")
    assert response.status_code == 404, response.text


def test_course_section_crud(client):
    payload = {
        "course_section_name": "Python datetime module",
        "date_published": "2021-08-14",
        "last_updated": "2021-08-14",
        "course_section_is_draft": False,
        "course_section_is_complete": True,
        "course_section_purpose": "train student on datetimes",
        "course_section_order": 1,
    }
    response = client.post("/course-section", json=payload)
    assert response.status_code == 201, response.text
    assert response.json() == {"success": True, "created_id": 1}
    response = client.get("/course-section/1")
    data = response.json()
    expected = {
        "id": 1,
        "last_updated": "2021-08-14",
        "course_section_is_draft": False,
        "course_section_purpose": "train student on datetimes",
        "course_section_name": "Python datetime module",
        "date_published": "2021-08-14",
        "course_section_is_complete": True,
        "course_section_order": 1,
    }
    assert response.status_code == 200, response.text
    assert data == expected
    response = client.delete("/course-section/1")
    assert response.status_code == 204, response.text
    assert response.json() == {"success": True}
    response = client.get("/course-section/1")
    assert response.status_code == 404, response.text
