
import uuid
from sqlalchemy import Column, TIMESTAMP, func, String, BIGINT
from src.db import Base


class UserData(Base):
    __tablename__ = 'user'
    # __table_args__ = {'schema': "runtime_schema_name"}
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    user_id = Column("user_id", String, primary_key=True, nullable=False)
    user_name = Column("user_name", String, nullable=False)
    user_role = Column("user_role", String, nullable=False)
    user_email = Column("user_email", String, nullable=False)
    created = Column(TIMESTAMP, default=func.now(), nullable=False) #joined
    first_login = Column(TIMESTAMP,default=func.now(), nullable=True)
    last_login = Column(TIMESTAMP, nullable=True)
