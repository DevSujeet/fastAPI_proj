    # record_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    # record_type = Column("record_type", String, nullable=True)
    # record_category = Column("record_category", String, nullable=True)
    # record_subcategory = Column("record_subcategory", String, nullable=True)
    # file_name = Column("file_name", String, nullable=True)
    # file_type = Column("file_type", String, nullable=True)
    # submitted_date = Column(TIMESTAMP, default=func.now(), nullable=False)
    # record_date = Column(TIMESTAMP, default=func.now(), nullable=False)
    # active = Column("active", bool, default=True)


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

    @computed_field(return_type=str)
    @property
    def complete_address(self):
        """Getter for the complete address. this also be part of the json/model dump"""
        return f"{self.public_land_address}, {self.suburb}, {self.state}, {self.postalcode} "
    
    class Config:
        from_attributes = True
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.timestamp() * 1000,
        }