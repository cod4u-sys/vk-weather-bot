import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import UserInfo

load_dotenv()

DATABASE_PATH = os.getenv("DB_PATH")
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
Session = sessionmaker(bind=engine)

class UserServices:
    @staticmethod
    def get_user_by_id(user_id):
        session = Session()
        user = session.query(UserInfo).get(user_id)
        session.close()
        return user 
    
    @staticmethod
    def add_user(user_id, username, city_name="Москва", latitude=55.75, longitude=37.62):
        session = Session()
        user = UserInfo(id=user_id, username=username, city_name=city_name, latitude=latitude, longitude=longitude)
        session.add(user)
        session.commit()
        session.close()
    
    @staticmethod
    def change_cityname(user_id, city_name="Москва", latitude=55.75, longitude=37.62):
        session = Session()
        user = session.query(UserInfo).get(user_id)
        user.city_name = city_name
        user.latitude = latitude
        user.longitude = longitude
        session.commit()
        session.close()
    @staticmethod
    def change_username(user_id, username):
        session = Session()
        user = session.query(UserInfo).get(user_id)
        user.username = username
        session.commit()
        session.close()