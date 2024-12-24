import uuid
from sqlalchemy import Column, TIMESTAMP, func, String, BIGINT
from src.db import Base

class LocationData(Base):
    __tablename__ = 'location'

    location_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    adbor_id = Column("adbor_id", String, primary_key=True, nullable=True)
    property_name = Column("property_name", String, nullable=True)
    address_type = Column("address_type", String, nullable=True)
    public_land_address = Column("public_land_address", String, nullable=True)
    state = Column("state", String, nullable=True)
    suburb = Column("suburb", String, nullable=True)
    postalcode = Column("postalcode", int, nullable=True)


    submitted_date = Column(TIMESTAMP, default=func.now(), nullable=False)