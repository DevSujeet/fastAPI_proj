from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    user_id:str = Field(default=None, primary_key=True)
    user_name:str
    user_role:str
    user_email:EmailStr