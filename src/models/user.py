from pydantic import BaseModel
import time
from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    user_id:str = Field(default=None, primary_key=True)
    user_name:str
    user_role:str
    user_email:EmailStr