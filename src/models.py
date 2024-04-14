from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///user_database.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    mobile_number = Column(String)
    crop_type = Column(String)

class UserData(Base):
    __tablename__ = 'user_data'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

