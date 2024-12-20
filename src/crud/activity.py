from fastapi import HTTPException
from src.crud.base_curd import BaseCRUD
from src.models.UserActivity import UserActivityBase, UserActivity
from sqlmodel import select

class UserActivityCRUD(BaseCRUD):

    def create_user_activity(self, activity:UserActivityBase):
        activity_obj = UserActivity(user_id=activity.user_id,
                            record_name=activity.record_name,
                            data_category=activity.data_category,
                            action=activity.action,
                            timestamp=activity.timestamp)

        self.db_session.add(activity_obj)

        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(activity)
        
    
    def get_all_user_activity(self):
        statement = select(UserActivity)
        results = self.db_session.exec(statement=statement)
        return results
    
    def get_activities_by_user(self, user_id:str):
        statement = select(UserActivity).where(UserActivity.user_id == user_id)
        results = self.db_session.exec(statement=statement)
        activities = results.all
        if activities is None:
            raise HTTPException(status_code=404, detail='some error occured while getting activities of the user')
        return activities
