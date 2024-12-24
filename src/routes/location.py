from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.schemas.location import Location
from typing import List

from src.services.user import create_user, get_all_user, get_user_by_id

router = APIRouter(
    prefix="/location",
    tags=["location"],
    responses={404: {"description": "location not in db"}}
)

@router.get('/all')
async def all_Location() -> List[Location]:
   print(f'get all records')

@router.get('')
async def get_location_by_id(id:str) -> Location:
    # return record for a given id
    print(f'return record for a given id')

@router.post('')
async def create_location_entry(user:Location) -> Location:
    print(f'create a record entry')