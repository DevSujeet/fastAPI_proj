# from pydantic import BaseModel
import uuid
from datetime import datetime
from pydantic import EmailStr
from enum import Enum
from sqlmodel import SQLModel, Field
from src.models.user import User  # Import User class

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
    id:int = Field(default_factory=uuid.uuid4, primary_key=True)


