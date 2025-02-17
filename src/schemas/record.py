
from pydantic import BaseModel, computed_field
from datetime import datetime
from typing import List, Optional


class Record(BaseModel):
    record_type:str
    record_category:str
    record_subcategory:Optional[str]
    file_name:str
    file_type:Optional[str]
    active:bool
    record_date: Optional[datetime]
    submitted_date: Optional[datetime]

    #use these for association tables
    project_id: Optional[str] = None # project id, check if this is needed when creating a record-or -take obj instead?
    locations: Optional[List[str]] = None # location_ids, check if this is needed when creating a record- or -- take obj instead?

    class Config:
        from_attributes = True #'orm_mode' has been renamed to 'from_attributes'
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.timestamp() * 1000,
        }

class RecordResponse(Record):
    record_id:str

    # class Config:
    #     from_attributes = True  # Ensures attributes are mapped properly
    #     use_enum_values = True