from fastapi import HTTPException
from src.crud.base_curd import BaseCRUD
from src.models.user import User
from sqlmodel import select

class UserCRUD(BaseCRUD):

    def create_user(self, user:User):
        print(f'create_user in crud pre{user}')
        self.db_session.add(user)
        print(f'create_user in crud post{user}')
        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(user)
        print(f'user is created {user}')
        return user
    
    def get_all_user(self):
        statement = select(User)
        results = self.db_session.exec(statement=statement)
        return results
    
    def get_user(self, user_id:str):
        statement = select(User).where(User.user_id == user_id)
        results = self.db_session.exec(statement=statement)
        user = results.first()
        if user is None:
            raise HTTPException(status_code=404, detail='user not found')
        return user
