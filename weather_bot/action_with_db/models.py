import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Text, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

load_dotenv()

DATABASE_PATH = os.getenv("DB_PATH")
Base = declarative_base()
engine = create_engine(f"sqlite:///{DATABASE_PATH}")

class UserInfo(Base):
    """Создание таблицы в базе данных bot.db"""
    __tablename__ = "users_info"
    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    city_name = Column(Text, nullable=False, default="Москва")
    latitude = Column(Float, default=55.75)
    longitude = Column(Float, default=37.62)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<{self.username, self.id}>"
    
Base.metadata.create_all(engine)
