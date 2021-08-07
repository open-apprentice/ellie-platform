from typing import List

from datetime import date
from pydantic import BaseModel

class CreateCourse(BaseModel):
    course_name: str
    is_draft: bool
    is_published: bool 
    date_published: date = None
    last_updated: date = None 
    author: str
    # course_sections: List[str] = []
    
    