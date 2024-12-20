from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.models.user import User
from typing import List
from src.db import get_session
from sqlmodel import Session

from src.services.user import create_user, get_all_user, get_user_by_id

router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_session)],
    responses={404: {"description": "user not in db"}}
)

@router.get('/all')
async def allUsers(session:Session = Depends(get_session)) -> List[User]:
    users = get_all_user(session=session)
    return users

@router.get('')
async def user(id:str, session:Session = Depends(get_session)) -> User:
    # return user for a given user_id
    user = get_user_by_id(id=id, session=session)
    return user

@router.post('')
async def create_user_entry(user:User, session:Session = Depends(get_session)) -> User:
    user = create_user(user=user, session=session)
    return user
