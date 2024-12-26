from src.db import get_session
from src.schemas.location import Location
from src.crud.location import LocationCRUD

def all_Location():
    with get_session() as session:
        location = LocationCRUD(db_session=session).get_all_location()
        return location

def get_location_by_id(id:str):
     with get_session() as session:
        location = LocationCRUD(db_session=session).get_location(location_id=id)
        return location

def create_location_entry(location=Location):
    with get_session() as session:
        location = LocationCRUD(db_session=session).create_location(location=location)
        return location