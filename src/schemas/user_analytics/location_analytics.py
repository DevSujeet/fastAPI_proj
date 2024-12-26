from pydantic import BaseModel
from typing import Optional, List
from src.schemas.location import Location



class LocationOverViewResponse(BaseModel):
    active: Optional[List[Location]]
    completed: Optional[List[Location]]
    on_hold: Optional[List[Location]]