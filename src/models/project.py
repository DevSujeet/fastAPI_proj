import uuid
from sqlalchemy import Column, TIMESTAMP, func, String, BIGINT
from src.db import Base

class ProjectData(Base):
    __tablename__ = 'project'

    project_system_id = Column('project_system_id',String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    project_id = Column("project_id", String, primary_key=True, nullable=False)
    project_title = Column("project_title", String, nullable=False)
    project_status = Column("project_status", String, nullable=False)
    created = Column(TIMESTAMP, default=func.now(), nullable=False)
