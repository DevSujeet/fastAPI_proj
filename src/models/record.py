import uuid
from sqlalchemy import Column, TIMESTAMP, func, String
from src.db import Base


class RecordData(Base):
    __tablename__ = 'record'
    record_id = Column('record_id', String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    record_type = Column("record_type", String, nullable=True)
    record_category = Column("record_category", String, nullable=True)
    record_subcategory = Column("record_subcategory", String, nullable=True)
    file_name = Column("file_name", String, nullable=True)
    file_type = Column("file_type", String, nullable=True)
    submitted_date = Column(TIMESTAMP, default=func.now(), nullable=False)
    record_date = Column(TIMESTAMP, default=func.now(), nullable=False)
    active = Column("active", bool, default=True)
    