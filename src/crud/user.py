
from sqlalchemy import and_, asc
from src.crud.base_curd import BaseCRUD
from src.models.user import UserData
from src.schemas.user import User

class UserCRUD(BaseCRUD):

    def create_user(self, user:User):
        print(f'create_user in crud pre{user}')
        user_obj = UserData(**user)
        self.db_session.add(user_obj)
        print(f'create_user in crud post{user_obj}')
        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(user_obj)
        print(f'user is created {user_obj}')
        return user_obj
    
    def get_all_user(self):
        # statement = select(User)
        # results = self.db_session.exec(statement=statement)
        query = self.db_session.query(UserData).order_by(asc(UserData.created))
        return query.all()
    
    def get_user(self, user_id:str):
        filters = []
        if user_id:
            filters.append(UserData.user_id == user_id)
        query = self.db_session.query(UserData).filter(and_(*filters)).order_by(asc(UserData.created))
        return query.all()
