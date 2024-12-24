from pydantic import BaseModel
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional, List
from src.schemas.location import Location
from src.schemas.project import Project


class LocationOverViewResponse(BaseModel):
    active: Optional[List[Location]]
    completed: Optional[List[Location]]
    on_hold: Optional[List[Location]]