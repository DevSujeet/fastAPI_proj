from fastapi import HTTPException
from sqlalchemy import and_, asc
from src.schemas.pagination.pagination import PageParams,paginate
from src.schemas.record import Record, RecordResponse
from src.models.record import RecordData
from src.crud.base_curd import BaseCRUD

class RecordCRUD(BaseCRUD):
   
    def get_all_record(self, page_params: PageParams):
        query = self.db_session.query(RecordData).order_by(asc(RecordData.submitted_date))
        return paginate(page_params=page_params, query=query, model=RecordData, ResponseSchema=RecordResponse)
        # return query.all()

    def get_record_by_id(self, record_id:str):
        if not id:
            raise HTTPException(status_code=400, detail="Record ID must be provided")
    
        filters = [RecordData.record_id == record_id]
        query = self.db_session.query(RecordData).filter(and_(*filters)).order_by(asc(RecordData.submitted_date))
        record = query.first()
        if record:
            return record
        else:
            raise HTTPException(status_code=404, detail="Record not found")

    def create_record_entry(self, record:Record):
        record_obj = RecordData(**record.model_dump(exclude={"locations", "project_id"}))
        self.db_session.add(record_obj)
        print(f'create_record in crud post{record_obj}')
        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(record_obj)
        print(f'record is created {record_obj}')
        return record_obj
    
    def delete_record_by_id(self, record_id:str):
        record = self.get_record_by_id(record_id=record_id)
        if record:
            self.db_session.delete(record)
            self.db_session.commit()
            return record
        else:
            raise HTTPException(status_code=404, detail="Record not found")