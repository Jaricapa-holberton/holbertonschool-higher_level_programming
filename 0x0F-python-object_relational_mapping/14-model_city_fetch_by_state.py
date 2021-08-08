#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


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
    citiesStates = session.query(City, State) \
        .filter(City.state_id == State.id) \
        .order_by(City.id)
    # Print results
    for city, state in citiesStates:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
