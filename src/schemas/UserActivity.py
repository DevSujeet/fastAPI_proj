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

class ActionType(Enum):
    DOWNLOAD = "DOWNLOAD"
    UPLOAD = "UPLOAD"
    CREATE = "CREATE"
    EDIT = "EDIT"
    DELETE = "DELETE"
    SEARCH = "SEARCH"

class UserActivityBase(SQLModel):
    user_id:str = Field(foreign_key="user.user_id")
    record_name:str #file name that was uploaded
    data_category:str
    action:ActionType
    timestamp:datetime

class UserActivity(UserActivityBase,table=True):
    id:int = Field(default=None, primary_key=True)


