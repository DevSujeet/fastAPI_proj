from fastapi import HTTPException
from sqlalchemy import and_, asc
from src.schemas.record import Record, RecordCreate
from src.models.record import RecordData
from src.crud.base_curd import BaseCRUD

class RecordCRUD(BaseCRUD):
   
    def allRecord(self):
        query = self.db_session.query(RecordData).order_by(asc(RecordData.submitted_date))
        return query.all()

    def get_record_by_id(self, id:str):
        if not id:
            raise HTTPException(status_code=400, detail="Record ID must be provided")
    
        filters = [RecordData.id == id]
        query = self.db_session.query(RecordData).filter(and_(*filters)).order_by(asc(RecordData.submitted_date))
        record = query.first()
        if record:
            return record
        else:
            raise HTTPException(status_code=404, detail="Record not found")

    def create_record_entry(self, record:RecordCreate):
        record_obj = RecordData(**record.model_dump())
        self.db_session.add(record_obj)
        print(f'create_record in crud post{record_obj}')
        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(record_obj)
        print(f'record is created {record_obj}')
        return record_obj
    
    def delete_record_by_id(self, id:str):
        record = self.get_record_by_id(id=id)
        if record:
            self.db_session.delete(record)
            self.db_session.commit()
            return record
        else:
            raise HTTPException(status_code=404, detail="Record not found")