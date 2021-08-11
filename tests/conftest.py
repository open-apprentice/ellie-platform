from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from models.courses import Base

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
