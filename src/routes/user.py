from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.config.configs import _db_settings
from typing import Dict
from src.schemas.UserActivity import User
from typing import List

import os

router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(get_project_header)],
    # responses={404: {"description": "X_ProjectID field is required in header"}}
)

USERS = [
    User(user_id='1', user_name='sunny',user_role='admin', user_email='sunny@gmail.com'),
    User(user_id='2', user_name='amit',user_role='developer', user_email='amit@gmail.com'),
    User(user_id='3', user_name='amarjeet',user_role='sales', user_email='amarjeet@gmail.com'),
    User(user_id='4', user_name='ritesh',user_role='sales', user_email='ritesh@gmail.com'),
]

@router.get('/all')
async def allUsers() -> List[User]:
    return USERS
    

@router.get('')
async def user(id:str) -> User:
    # return user for a given user_id
    return USERS[1]

@router.post('')
async def create_user(user:User) -> User:
    USERS.append(user)
    return user