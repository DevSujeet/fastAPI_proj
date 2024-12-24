from fastapi import APIRouter, Depends
from fastapi.logger import logger
from typing import Dict
from src.schemas.user_activity import UserActivityResponse, UserActivityCreate
from typing import List
from src.services.userActivity import insert_user_activity, get_activities_by_userid, get_all_user_activities
from src.db import get_session

router = APIRouter(
    prefix="/activity",
    tags=["activity"],
    responses={404: {"description": "user_id field is required."}}
)

@router.get('/all')
async def all_users_activities() -> List[UserActivityResponse]:
    return get_all_user_activities()
    

@router.get('/byUser')
async def activity_by_user(user_id:str) -> List[UserActivityResponse]:
    # return user for a given user_id
    return get_activities_by_userid(user_id=user_id)

@router.post('')
async def create_user_activity(activity:UserActivityCreate):
    insert_user_activity(activity=activity)