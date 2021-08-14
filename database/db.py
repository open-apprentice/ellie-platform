import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]
Base = declarative_base()


def validate_database():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    if not database_exists(engine.url):
        create_database(engine.url)
        print("New Database Created" + database_exists(engine.url))
    else:
        print("Database already exists")


def _init_db(db_url):
    engine = create_engine(db_url)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)()


def get_db(db_url=None):
    if db_url is None:
        db_url = SQLALCHEMY_DATABASE_URL
    db = _init_db(db_url)
    try:
        yield db
    except Exception as exc:
        print(exc)
        raise
    finally:
        db.close()
