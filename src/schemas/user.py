from pydantic import BaseModel,Field,EmailStr
from src.enum.general import UserRole

class User(BaseModel):
    user_id:str
    user_name:str
    user_role:UserRole
    user_email:EmailStr

    class Config:
        from_attributes = True