from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.schemas.record import Record
from typing import List
from src.db import get_session
from sqlmodel import Session

from src.services.user import create_user, get_all_user, get_user_by_id

router = APIRouter(
    prefix="/record",
    tags=["user"],
    responses={404: {"description": "record not in db"}}
)

@router.get('/all')
async def allRecord() -> List[Record]:
   print(f'get all records')

@router.get('')
async def get_record_by_id(id:str) -> Record:
    # return record for a given id
    print(f'return record for a given id')

@router.post('')
async def create_record_entry(record:Record) -> Record:
    print(f'create a record entry')
