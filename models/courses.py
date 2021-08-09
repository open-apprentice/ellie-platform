from sqlalchemy import Integer, String, Boolean, Date, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
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
    # QUESTION: Many course sections to one Course below - many to one relationship
    # QUESTION (Continue) This looks like the opposite of this: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-one and I am confused... totally.
    # QUESTION: Should the below many to one relationship work? How do I test this?
    # QUESTION: How does the below relate to this: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-relationships? Do I use `back_populates`?
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", backref="course-sections")

    # QUESTION: I ask this later, but should I be including this in the code? And how do I find out in english what this does? refering to def __init__?
    def __init__(
        self,
        course_section_name,
        date_published,
        last_updated,
        course_section_is_draft,
        course_section_is_complete,
        course_section_purpose,
        course_section_order,
    ):
        self.course_section_name = course_section_name
        self.date_published = date_published
        self.last_updated = last_updated
        self.course_section_is_draft = course_section_is_draft
        self.course_section_is_complete = course_section_is_complete
        self.course_section_purpose = course_section_purpose
        self.course_section_order = course_section_order


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

    # QUESTION: Should I be doing this? def __init__() below?
    # QUESTION: Should or when should I use "-> None:"?? Am I type checking with this library?
    # Ref: https://stackoverflow.com/questions/64933298/why-should-we-use-in-def-init-self-n-none
    def __init__(self, course_name, is_draft, is_published, last_updated, author):
        self.course_name = course_name
        self.is_draft = is_draft
        self.is_published = is_published
        self.last_updated = last_updated
        self.author = author
