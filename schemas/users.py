from pydantic import BaseModel
from pydantic.networks import EmailStr

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    is_admin: bool
    user_email: EmailStr
