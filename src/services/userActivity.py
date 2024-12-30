from src.crud.activity import UserActivityCRUD
from src.schemas.user_activity import UserActivityCreate
# from sqlmodel import Session
from src.db import get_session

def create_user_activity(activity:UserActivityCreate):
    with get_session() as session:
        activity_curd = UserActivityCRUD(db_session=session)
        activity_curd.create_user_activity(activity=activity)
    

def get_all_user_activities(user_id:str):
    with get_session() as session:
        activity_curd = UserActivityCRUD(db_session=session)
        activities = activity_curd.get_all_user_activity()
        return activities

def get_activities_by_userid(user_id:str):
    with get_session() as session:
        activity_curd = UserActivityCRUD(db_session=session)
        activities = activity_curd.get_activities_by_user(user_id=user_id)
        return activities