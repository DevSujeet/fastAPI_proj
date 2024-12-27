from pydantic import BaseModel, Field
from datetime import datetime
from src.enum.project_status import ProjectStatus
from typing import Optional, List
from src.enum.project_status import ProjectStatus

class Project(BaseModel):
    project_id:str #unique id provided by client while creating
    project_title:str
    project_status:ProjectStatus = Field(default=ProjectStatus.ACTIVE)
    created: Optional[datetime]
    # also will have a list of location ids
    locations: Optional[List[str]] = []

    class Config:
        from_attributes = True #'orm_mode' has been renamed to 'from_attributes'
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.timestamp() * 1000,
        }


class ProjectCreate(Project):
    user_id: str