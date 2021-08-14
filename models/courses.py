from sqlalchemy import Integer, String, Boolean, Date, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from database.db import Base


course_sections_table = Table('course_sections_association', Base.metadata,
    Column('course_id', ForeignKey('course.id'), primary_key=True),
    Column('course_sections_id', ForeignKey('course_sections.id'), primary_key=True)
)


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    is_draft = Column(Boolean, default=False)
    is_published = Column(Boolean, default=False)
    date_published = Column(Date)
    last_updated = Column(Date)
    # TODO: make this foreign key to User table
    author = Column(String, nullable=False)
    course_sections = relationship("CreateCourseSection",
                                   secondary=course_sections_table,
                                   back_populates="courses")


class CreateCourseSection(Base):
    __tablename__ = "course_sections"

    id = Column(Integer, primary_key=True)
    course_section_name = Column(String, nullable=False)
    date_published = Column(Date)
    last_updated = Column(Date)
    course_section_is_draft = Column(Boolean, default=False)
    course_section_is_complete = Column(Boolean, default=False)
    course_section_purpose = Column(String, nullable=False)
    course_section_order = Column(Integer, nullable=False)
    courses = relationship("Course",
                           secondary=course_sections_table,
                           back_populates="course_sections")
