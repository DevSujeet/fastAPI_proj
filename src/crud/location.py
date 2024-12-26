from sqlalchemy import and_, asc
from src.models.location import LocationData
from src.schemas.location import Location
from src.crud.base_curd import BaseCRUD

class LocationCRUD(BaseCRUD):
    def all_Location(self):
        query = self.db_session.query(LocationData).order_by(asc(LocationData.submitted_date))
        return query.all()

    def get_location_by_id(self, id:str):
        filters = []
        if id:
            filters.append(LocationData.location_id == id)
        query = self.db_session.query(LocationData).filter(and_(*filters)).order_by(asc(LocationData.submitted_date))
        return query.all()

    def create_location_entry(self, location=Location):
        location_obj = LocationData(**location)
        self.db_session.add(location_obj)
        print(f'create_location in crud post{location_obj}')
        self.db_session.flush()
        self.db_session.commit()
        self.db_session.refresh(location_obj)
        print(f'location is created {location_obj}')
        return location_obj