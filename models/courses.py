from sqlalchemy import Integer, String, Boolean, Date
from sqlalchemy.sql.schema import Column

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CreateCourseSection(Base):
    __tablename__ = "course-sections"

    id = Column(Integer, primary_key=True)
    course_section_name = Column(String, nullable=False)
    date_published = Column(Date)
    last_updated = Column(Date)
    course_section_is_draft = Column(Boolean, default=False)
    course_section_is_complete = Column(Boolean, default=False)
    course_section_purpose = Column(String, nullable=False)
    course_section_order = Column(Integer, nullable=False)
    # This needs a way to assign to a specific course


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    is_draft = Column(Boolean, default=False)
    is_published = Column(Boolean, default=False)
    date_published = Column(Date)
    last_updated = Column(Date)
    author = Column(String, nullable=False)
    # This would have a list of all the CreateCourseSections that have been made and assigned to this course.
    # https://github.com/tiangolo/fastapi/issues/2194
    # created_course_sections = Column(???, nullable=True) ???
