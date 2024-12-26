from src.db import get_session
from src.schemas.record import Record
from src.crud.record import RecordCRUD

def allRecord():
     with get_session() as session:
        records = RecordCRUD(db_session=session).get_all_record()
        return records

def get_record_by_id(id:str):
     with get_session() as session:
        record = RecordCRUD(db_session=session).get_record(record_id=id)
        return record

def create_record_entry(record:Record):
     with get_session() as session:
        record = RecordCRUD(db_session=session).create_record(record=record)
        return record