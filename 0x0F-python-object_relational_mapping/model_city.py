#!/usr/bin/python3
"""
Define City Class and an instance Base
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# instance the Base obect from SQLAlchemy
Base = declarative_base()

# the class inherits from Base


class City(Base):
    """Represent a city"""
    # links to the MySQL table states
    __tablename__ = "cities"
    # create the columns properties
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
