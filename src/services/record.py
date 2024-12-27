from src.crud.activity import UserActivityCRUD
from src.db import get_session
from src.enum.actions import ActionType
from src.schemas.record import Record, RecordCreate
from src.crud.record import RecordCRUD
from src.schemas.user_activity import UserActivityCreate


def allRecord():
     with get_session() as session:
        records = RecordCRUD(db_session=session).get_all_record()
        return records

def get_record_by_id(user_id:str, id:str):
     with get_session() as session:
        record = RecordCRUD(db_session=session).get_record(record_id=id)
        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           record_id=id,
                                           action=ActionType.SEARCH)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        return record

def create_record_entry(record:RecordCreate):
     with get_session() as session:
        record_obj = RecordCRUD(db_session=session).create_record_entry(record=record)
         # create user activity
        user_activity = UserActivityCreate(user_id=record.user_id,
                                           record_id=record_obj.record_id,
                                           action=ActionType.CREATE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        return record_obj
     
def delete_record_entry(user_id:str, id:str):
     with get_session() as session:
        record = RecordCRUD(db_session=session).delete_record(record_id=id)
         # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           location_id=id,
                                           action=ActionType.DELETE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        return record