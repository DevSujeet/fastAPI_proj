from src.crud.activity import UserActivityCRUD
from src.db import get_session
from src.enum.actions import ActionType
from src.schemas.location import Location,LocationCreate
from src.crud.location import LocationCRUD
from src.schemas.user_activity import UserActivityCreate

def all_Location():
    with get_session() as session:
        location = LocationCRUD(db_session=session).get_all_location()
        return location

def get_location_by_id(user_id:str, id:str):
     with get_session() as session:
        location = LocationCRUD(db_session=session).get_location_by_id(location_id=id)

        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           location_id=id,
                                           action=ActionType.SEARCH)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        
        return location

def create_location_entry(location=LocationCreate):
    with get_session() as session:
        location_obj = LocationCRUD(db_session=session).create_location_entry(location=location)
        # create user activity
        user_activity = UserActivityCreate(user_id=location.user_id,
                                           location_id=location_obj.location_id,
                                           action=ActionType.CREATE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        return location
    

def delete_location_by_id(user_id:str, location_id:str):
    with get_session() as session:
        location = LocationCRUD(db_session=session).delete_location_by_id(location_id=id)
        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           location_id=location_id,
                                           action=ActionType.DELETE)
        
        return location