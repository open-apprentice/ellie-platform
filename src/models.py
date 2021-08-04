from sqlalchemy import Integer, String, Boolean
from sqlalchemy_utils import EmailType
from sqlalchemy.sql.schema import Column
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    user_email = Column(EmailType, nullable=False)
    
    