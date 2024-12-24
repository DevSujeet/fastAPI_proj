from pydantic import BaseModel, computed_field
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional, List


class Location(BaseModel):
    location_id:str
    adbor_id:Optional[str]
    property_name:str
    address_type:Optional[str]
    public_land_address:Optional[str]
    state:Optional[str]
    suburb:Optional[str]
    postalcode:Optional[int]
    submitted_date: Optional[datetime]

    @computed_field(return_type=str)
    @property
    def complete_address(self) -> str:
        """Getter for the complete address. this also be part of the json/model dump"""
        return f"{self.public_land_address}, {self.suburb}, {self.state}, {self.postalcode} "
    
    class Config:
        orm_mode = True
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.timestamp() * 1000,
        }