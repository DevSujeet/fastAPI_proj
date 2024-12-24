from fastapi import APIRouter, Depends
from fastapi.logger import logger
from src.schemas.user import User
from typing import List


from src.services.user import create_user, get_all_user, get_user_by_id

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "user not in db"}}
)

@router.get('/all')
async def allUsers() -> List[User]:
    users = get_all_user()
    return users

@router.get('')
async def user(id:str) -> User:
    # return user for a given user_id
    user = get_user_by_id(id=id)
    return user

@router.post('')
async def create_user_entry(user:User) -> User:
    user = create_user(user=user)
    return user
