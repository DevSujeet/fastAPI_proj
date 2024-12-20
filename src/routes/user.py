from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.config.configs import _db_settings
from typing import Dict
from src.models.user import User
from typing import List
from src.crud.user import UserCRUD
from src.db import get_session
from sqlmodel import Session

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
async def allUsers(session:Session = Depends(get_session)) -> List[User]:
    # return USERS
    user_curd = UserCRUD(db_session=session)
    users = user_curd.get_all_user()
    return users

    

@router.get('')
async def user(id:str, session:Session = Depends(get_session)) -> User:
    # return user for a given user_id
    user_curd = UserCRUD(db_session=session)
    user = user_curd.get_user(user_id=id)
    return user

@router.post('')
async def create_user(user:User, session:Session = Depends(get_session)) -> User:
    # USERS.append(user)
    # return user
    user_curd = UserCRUD(db_session=session)
    user_curd.create_user(user=user)
    return user
