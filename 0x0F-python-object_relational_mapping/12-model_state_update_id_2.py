#!/usr/bin/python3
"""
Change the name of a State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    """
    Print the State object with the name passed as argument
    from the database hbtn_0e_6_usa
    """
    # Create engine. The args comes from input
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # Start Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
