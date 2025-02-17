

import uuid
from sqlalchemy import Column, String, INT, ForeignKey
from src.db import Base

class ProjectLocationData(Base):
    __tablename__ = 'project_location'

    project_location_id = Column('project_location_id', String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    location_id = Column("location_id", String, ForeignKey("location.location_id"), nullable=True) #foriegn key to location table location_id
    project_id = Column("project_id", String, ForeignKey("project.project_system_id"), nullable=True) #foriegn key to location table location_id
    location_type = Column("location_type", String, nullable=True)
