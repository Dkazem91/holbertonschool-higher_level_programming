#!/usr/bin/python3
# sqlalchemy stuff
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    state = session.query(State).filter(
        State.name == sys.argv[4]).all()
    if state:
        for place in state:
            print("{}".format(place.id))
    else:
        print("Not Found")
    session.close()
