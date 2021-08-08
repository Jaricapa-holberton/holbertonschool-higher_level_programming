#!/usr/bin/python3
"""
Define State Class and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# instance the Base obect from SQLAlchemy
Base = declarative_base()

# the class inherits from Base


class State(Base):
    """Represent a state object"""

    # links to the MySQL table states
    __tablename__ = "states"
    # create the columns properties
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
