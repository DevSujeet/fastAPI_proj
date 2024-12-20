from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.config.configs import _db_settings
from typing import Dict
from src.models.UserActivity import UserActivityBase, ActionType
from datetime import datetime
from typing import List

import os

router = APIRouter(
    prefix="/activity",
    tags=["activity"],
    # dependencies=[Depends(get_project_header)],
    # responses={404: {"description": "X_ProjectID field is required in header"}}
)

ACTIVITIES = [
    UserActivityBase(user_id='1',record_name="abc.pdf",data_category='govt',action=ActionType.EDIT,timestamp=datetime.now()),
    UserActivityBase(user_id='2',record_name="bsd.pdf",data_category='pvt',action=ActionType.CREATE,timestamp=datetime.now()),
    UserActivityBase(user_id='3',record_name="ert.pdf",data_category='public',action=ActionType.UPLOAD,timestamp=datetime.now()),
    UserActivityBase(user_id='4',record_name="fgt.pdf",data_category='govt',action=ActionType.DELETE,timestamp=datetime.now()),
]

@router.get('/all')
async def allUsers() -> List[UserActivityBase]:
    return ACTIVITIES
    

@router.get('/byUser')
async def userActivity_byUser(user_id:str) -> UserActivityBase:
    # return user for a given user_id
    return ACTIVITIES[1]

@router.post('')
async def create_user(activity:UserActivityBase) -> UserActivityBase:
    ACTIVITIES.append(activity)
    return activity