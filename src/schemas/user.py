from pydantic import BaseModel,Field,EmailStr

class User(BaseModel):
    user_id:str
    user_name:str
    user_role:str
    user_email:EmailStr