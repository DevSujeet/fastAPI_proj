from fastapi import APIRouter, Depends
from fastapi.logger import logger
from typing import Dict
from src.dependencies import get_user_id_header
from src.schemas.user_activity import UserActivityResponse, UserActivityCreate
from typing import List
import src.services.userActivity as UserActivityService
from src.db import get_session

router = APIRouter(
    prefix="/activity",
    tags=["activity"],
    dependencies=[Depends(get_user_id_header)],
    responses={404: {"description": "x_user_id field is required in header"}}
)

@router.get('/all')
async def all_users_activities(user_id=Depends(get_user_id_header)) -> List[UserActivityResponse]:
    activities = UserActivityService.get_all_user_activities(user_id=user_id)
    return activities
    

@router.get('/byUser')
async def activity_by_user(user_id=Depends(get_user_id_header)) -> List[UserActivityResponse]:
    # return user for a given user_id
    activity = UserActivityService.get_activities_by_userid(user_id=user_id)
    return activity

# @router.post('')
# async def create_user_activity(activity:UserActivityCreate):
#     UserActivityService.create_user_activity(activity=activity)