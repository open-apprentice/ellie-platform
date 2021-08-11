from datetime import datetime

import pytest

from models.courses import Base, Course, CreateCourseSection

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite://'


@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DB_URL, echo=True)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def session(engine):
    session = sessionmaker(bind=engine)()
    yield session
    session.rollback()


@pytest.fixture(scope="session", autouse=True)
def courses(session):
    courses = [
        Course(
            course_name="100 days of py",
            date_published=datetime.now(),
            last_updated=datetime.now(),
            author="bob, julian and mike",
            course_sections=[]
        ),
        Course(
            course_name="100 days of web",
            date_published=datetime.now(),
            last_updated=datetime.now(),
            author="bob, julian and mike",
            course_sections=[]
        ),
    ]
    for course in courses:
        session.add(course)
    session.commit()


@pytest.fixture(scope="session", autouse=True)
def sections(session):
    sections = [
        CreateCourseSection(
            course_section_name="datetimes",
            date_published=datetime.now(),
            last_updated=datetime.now(),
            course_section_purpose="work with datetimes",
            course_section_order=1,
            courses=[]),
        CreateCourseSection(
            course_section_name="itertools",
            date_published=datetime.now(),
            last_updated=datetime.now(),
            course_section_purpose="write functional code",
            course_section_order=2,
            courses=[]),
        CreateCourseSection(
            course_section_name="pytest",
            date_published=datetime.now(),
            last_updated=datetime.now(),
            course_section_purpose="write unit tests",
            course_section_order=3,
            courses=[]),
        CreateCourseSection(
            course_section_name="selenium",
            date_published=datetime.now(),
            last_updated=datetime.now(),
            course_section_purpose="write integration tests",
            course_section_order=4,
            courses=[])
    ]
    for section in sections:
        session.add(section)
    session.commit()


def test_create_courses(session):
    assert session.query(Course).count() == 2


def test_create_sections(session):
    assert session.query(CreateCourseSection).count() == 4


def test_assoc_relation_course_sections(session):
    first_course, second_course = session.query(Course).all()
    sections = session.query(CreateCourseSection).all()
    first_course.course_sections = sections[:2]
    second_course.course_sections = sections[2:]
    session.add(first_course)
    session.add(second_course)
    session.commit()

    first_course, second_course = session.query(Course).all()
    assert len(first_course.course_sections) == 2
    assert len(second_course.course_sections) == 2

    actual = [s.course_section_name for s in first_course.course_sections]
    expected = ["datetimes", "itertools"]
    assert actual == expected

    actual = [s.course_section_name for s in second_course.course_sections]
    expected = ["pytest", "selenium"]
    assert actual == expected
