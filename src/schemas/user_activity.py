from pydantic import BaseModel
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional

class UserActivityCreate(BaseModel):
    user_id: str
    record_id: Optional[str] = None
    project_id: Optional[str] = None
    location_id: Optional[str] = None
    action: ActionType

    class Config:
        from_attributes = True

class UserActivityResponse(BaseModel):
    id: int
    user_id: str
    record_id: Optional[str] = None
    project_id: Optional[str] = None
    location_id: Optional[str] = None
    action: ActionType
    created: datetime

    class Config:
        from_attributes = True
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.timestamp() * 1000,
        }


