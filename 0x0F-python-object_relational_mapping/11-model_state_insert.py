#!/usr/bin/python3
# sql alchemy 7
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ls = State(name='Louisiana')
    session.add(ls)
    session.commit()
    state = session.query(State).filter(
        State.name == 'Louisiana').first()
    print("{}".format(state.id))
    session.close()
