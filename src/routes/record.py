from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.schemas.record import Record, RecordCreate
from typing import List
from src.db import get_session
from sqlmodel import Session

from src.services.record import allRecord, get_record_by_id, create_record_entry

router = APIRouter(
    prefix="/record",
    tags=["record"],
    responses={404: {"description": "record not in db"}}
)

@router.post('')
async def create_record_entry(record:RecordCreate) -> Record:
    print(f'create a record entry')
    create_record_entry(record=record)
    return record

@router.get('/all')
async def allRecord() -> List[Record]:
   print(f'get all records')
   records = allRecord()
   return records

@router.get('')
async def get_record_by_id(user_id:str, id:str) -> Record:
    # return record for a given id
    print(f'return record for a given id')
    record = get_record_by_id(user_id=user_id, id=id)
    return record

