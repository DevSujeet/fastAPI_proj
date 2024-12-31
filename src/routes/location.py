from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.dependencies import get_user_id_header
from src.schemas.location import Location, LocationResponse
from typing import List

import src.services.location as location_service

router = APIRouter(
    prefix="/location",
    tags=["location"],
    dependencies=[Depends(get_user_id_header)],
    responses={404: {"description": "x_user_id field is required in header"}}
)

@router.post('')
async def create_location_entry(location:Location, user_id=Depends(get_user_id_header)) -> LocationResponse:
    print(f'create a location entry')
    location_obj = location_service.create_location_entry(location=location, user_id=user_id)
    return location_obj

@router.get('/all')
async def all_Location(user_id=Depends(get_user_id_header)) -> List[LocationResponse]:
   print(f'get all location')
   locations = location_service.all_Location(user_id=user_id)
   return locations


@router.get('')
async def get_location_by_id(id:str, user_id=Depends(get_user_id_header)) -> LocationResponse:
    print(f'return location for a given id')
    location = location_service.get_location_by_id(user_id=user_id, id=id)
    if location is None:
        raise BaseException
    return location

@router.delete('')
async def delete_location_by_id(id:str, user_id=Depends(get_user_id_header)) -> LocationResponse:
    print(f'delete location for a given id')
    location = location_service.delete_location_by_id(user_id=user_id, location_id=id)
    return location

