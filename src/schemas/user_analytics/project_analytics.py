from pydantic import BaseModel
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional, List
from src.enum.general import AddressType
from src.schemas.location import Location
from src.schemas.project import Project

# list of all the project by location
class ProjectsByLocationResponse(BaseModel):
    location_column: str # like state, postcode, lga
    location_value: str # like NSW, 2000, Sydney
    location_type: Optional[AddressType]
    projects: Optional[List[Project]]
    project_count: int

class ProjectStatusOverViewResponse(BaseModel):
    active: Optional[List[Project]]
    completed: Optional[List[Project]]
    on_hold: Optional[List[Project]]