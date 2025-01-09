from pydantic import BaseModel, computed_field
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional, List

from src.enum.general import AddressType


class ProjectLocationMapping(BaseModel):
    location_id:str
    property_id:str
    location_type:AddressType