from pydantic import BaseModel
from datetime import datetime
from src.enum.actions import ActionType
from typing import Optional, List, Dict

class UserRecordActivityResponse(BaseModel):
    id: int
    user_id: str
    record_name: Optional[str] = None # get record name fron record table by joining from record table and activity table on location_id
    action: ActionType
    created: datetime

    class Config:
        from_attributes = True #'orm_mode' has been renamed to 'from_attributes'

'''
{
    "values": [
        {
            "2024-12-24T00:00:00": [
                {
                    "key1": 10
                },
                {
                    "key2": 20
                }
            ]
        },
        {
            "2024-12-25T00:00:00": [
                {
                    "key3": 30
                },
                {
                    "key4": 40
                }
            ]
        }
    ]
}

'''
class UserUploadDownloadActivityResponse(BaseModel):
    values: List[Dict[datetime, List[Dict[str, int]]]]