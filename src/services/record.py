from src.crud.activity import UserActivityCRUD
from src.db import get_session
from src.enum.actions import ActionType
from src.schemas.record import Record
from src.crud.record import RecordCRUD
from src.schemas.user_activity import UserActivityCreate


def allRecord(user_id:str):
     with get_session() as session:
        records = RecordCRUD(db_session=session).get_all_record()
        return records

def get_record_by_id(user_id:str, record_id:str):
     with get_session() as session:
        record = RecordCRUD(db_session=session).get_record_by_id(record_id=record_id)
        # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           record_id=record_id,
                                           action=ActionType.SEARCH)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        return record

def create_record_entry(record:Record,user_id:str):
     with get_session() as session:
        record_obj = RecordCRUD(db_session=session).create_record_entry(record=record)
         # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           record_id=record_obj.record_id,
                                           action=ActionType.CREATE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        # TODO: add the entry to project location association table
        # or the record location group association table if the record is uploaded against a location group

        return record_obj
     
def delete_record_entry(user_id:str, record_id:str):
     with get_session() as session:
        record = RecordCRUD(db_session=session).delete_record_by_id(record_id=record_id)
         # create user activity
        user_activity = UserActivityCreate(user_id=user_id,
                                           record_id=record_id,
                                           action=ActionType.DELETE)
        UserActivityCRUD(db_session=session).create_user_activity(activity=user_activity)
        return record