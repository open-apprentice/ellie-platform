from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from sqlalchemy.sql.schema import Column, ForeignKey

from database.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    user_email = Column(EmailType, nullable=False)
    authors = relationship("Author", back_populates="user")
    students = relationship("Student", back_populates="user")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    created_courses = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="authors")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    enrolled_courses = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="students")
