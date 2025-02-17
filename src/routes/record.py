from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.dependencies import get_user_id_header
from src.schemas.pagination.pagination import PageParams, PagedResponseSchema
from src.schemas.record import Record, RecordResponse
from typing import List
from src.db import get_session
from sqlmodel import Session

import src.services.record as record_service

router = APIRouter(
    prefix="/record",
    tags=["record"],
    dependencies=[Depends(get_user_id_header)],
    responses={404: {"description": "x_user_id field is required in header"}}
)

@router.post('')
async def create_record_entry(record:Record, user_id=Depends(get_user_id_header)) -> RecordResponse:
    print(f'create a record entry')
    record_service.create_record_entry(record=record, user_id=user_id)
    return record

@router.post('/all', response_model=PagedResponseSchema[RecordResponse])
async def allRecord(page_params: PageParams, user_id=Depends(get_user_id_header)):
   print(f'get all records')
   records = record_service.allRecord(user_id=user_id, page_params=page_params)
   return records

@router.get('')
async def get_record_by_id(record_id:str, user_id=Depends(get_user_id_header)) -> RecordResponse:
    # return record for a given id
    print(f'return record for a given id')
    record = record_service.get_record_by_id(user_id=user_id, record_id=record_id)
    return record

