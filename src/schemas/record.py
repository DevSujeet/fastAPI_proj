
from pydantic import BaseModel, computed_field
from datetime import datetime
from typing import Optional


class Record(BaseModel):
    record_type:str
    record_category:str
    record_subcategory:Optional[str]
    file_name:str
    file_type:Optional[str]
    active:bool
    record_date: Optional[datetime]
    submitted_date: Optional[datetime]

    project_id:Optional[str] # project id, check if this is needed when creating a record-or -take obj instead?
    locations: Optional[str] # location_ids, check if this is needed when creating a record- or -- take obj instead?

    @computed_field(return_type=str)
    @property
    def complete_address(self):
        """Getter for the complete address. this also be part of the json/model dump"""
        return f"{self.public_land_address}, {self.suburb}, {self.state}, {self.postalcode} "
    
    class Config:
        from_attributes = True #'orm_mode' has been renamed to 'from_attributes'
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.timestamp() * 1000,
        }

class RecordCreate(Record):
    user_id: str

class RecordResponse(Record):
    record_id:str