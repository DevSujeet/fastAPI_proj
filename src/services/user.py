from src.crud.user import UserCRUD
from src.schemas.user import User
# from sqlmodel import Session
from src.db import get_session

def create_user(user:User) -> User:
    with get_session() as session:
        user_curd = UserCRUD(db_session=session)
        created_user = user_curd.create_user(user=user)
        return created_user

def get_all_user():
    with get_session() as session:
        user_curd = UserCRUD(db_session=session)
        users = user_curd.get_all_user()
        return users

def get_user_by_id(id:str):
    with get_session() as session:
        user_curd = UserCRUD(db_session=session)
        user = user_curd.get_user(user_id=id)
        return user