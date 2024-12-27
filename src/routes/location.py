from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.schemas.location import LocationCreate, Location
from typing import List

from src.services.location import all_Location, get_location_by_id, create_location_entry

router = APIRouter(
    prefix="/location",
    tags=["location"],
    responses={404: {"description": "location not in db"}}
)

@router.post('')
async def create_location_entry(location:LocationCreate) -> Location:
    print(f'create a record entry')
    location = create_location_entry(location=location)
    return location

@router.get('/all')
async def all_Location() -> List[Location]:
   print(f'get all records')
   locations = all_Location()
   return locations


@router.get('')
async def get_location_by_id(user_id:str, id:str) -> Location:
    # return record for a given id
    print(f'return record for a given id')
    location = get_location_by_id(user_id=user_id, id=id)
    if location is None:
        raise BaseException
    return location

