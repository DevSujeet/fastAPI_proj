from pydantic import BaseModel
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional, List
from src.schemas.location import Location
from src.schemas.project import Project

# list of all the project by location
class ProjectLocationsResponse(BaseModel):
    project_name: str
    locations: Optional[List[Location]]


class ProjectOverViewResponse(BaseModel):
    active: Optional[List[Project]]
    completed: Optional[List[Project]]
    on_hold: Optional[List[Project]]