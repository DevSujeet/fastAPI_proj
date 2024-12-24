from src.crud.activity import UserActivityCRUD
from src.models.UserActivity import UserActivityBase
# from sqlmodel import Session
from src.db import get_session

def insert_user_activity(activity:UserActivityBase):
    with get_session() as session:
        activity_curd = UserActivityCRUD(db_session=session)
        activity_curd.create_user_activity(activity=activity)
    

def get_all_user_activities():
    with get_session() as session:
        activity_curd = UserActivityCRUD(db_session=session)
        activities = activity_curd.get_all_user_activity()
        return activities

def get_activities_by_userid(user_id:str):
    with get_session() as session:
        activity_curd = UserActivityCRUD(db_session=session)
        activities = activity_curd.get_activities_by_user(user_id=user_id)
        return activities