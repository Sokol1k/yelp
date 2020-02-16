from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine("mysql+pymysql://root:@localhost:3306/yelp")

class Business(DeclarativeBase):
    __tablename__ = "business"

    id = Column(Integer, primary_key=True)
    name = Column('name', String, nullable=True)
    category = Column('category', String, nullable=True)
    address = Column('address', String, nullable=True)
    phone = Column('phone', String, nullable=True)
    reviews = Column('reviews', String, nullable=True)
    rating = Column('rating', String, nullable=True)
    image = Column('image', String, nullable=True)
    site = Column('site', String, nullable=True)
    workdays = Column('workdays', JSON, nullable=True)