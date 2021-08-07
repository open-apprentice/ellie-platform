from sqlalchemy import Integer, String, Boolean, Date
from sqlalchemy.sql.schema import Column

from database.db import Base


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    is_draft = Column(Boolean, default=False)
    is_published = Column(Boolean, default=False)
    date_published = Column(Date)
    last_updated = Column(Date)
    author = Column(String, nullable=False)
    # course_sections = Column()
    

    
    
    