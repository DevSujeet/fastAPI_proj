from pydantic import BaseModel
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional, List
from src.schemas.location import Location
from src.schemas.project import Project

# list of all the project by location
class ProjectsByLocationResponse(BaseModel):
    location: str
    location_id: str
    projects: Optional[List[Project]]

class ProjectsCountByLocationResponse(BaseModel):
    location_id: str
    location: str
    project_count: int

class ProjectStatusOverViewResponse(BaseModel):
    active: Optional[List[Project]]
    completed: Optional[List[Project]]
    on_hold: Optional[List[Project]]