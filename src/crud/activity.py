from fastapi import HTTPException
from sqlalchemy import and_, asc
from src.crud.base_curd import BaseCRUD
from src.models.UserActivity import UserActivityData
from src.schemas.user_activity import UserActivityCreate
# from sqlmodel import select

class UserActivityCRUD(BaseCRUD):

    def create_user_activity(self, activity:UserActivityCreate):
        activity_obj = UserActivityData(**activity)
        self.db_session.add(activity_obj)

        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(activity_obj)
        
    
    def get_all_user_activity(self):
        query = self.db_session.query(UserActivityData).order_by(asc(UserActivityData.created))
        return query.all()
    
    def get_activities_by_user(self, user_id:str):
        filters = []
        if user_id:
            filters.append(UserActivityData.user_id == user_id)
        query = self.db_session.query(UserActivityData).filter(and_(*filters)).order_by(asc(UserActivityData.created))
        activities = query.all()
        if activities is None:
            raise HTTPException(status_code=404, detail='some error occured while getting activities of the user')
        return activities
