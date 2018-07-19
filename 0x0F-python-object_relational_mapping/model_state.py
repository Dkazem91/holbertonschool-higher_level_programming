#!/usr/bin/python3
# sql alchemy awesome
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    # creates state
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


def __repr__(self):
    # reaper
    return "<States(id='%s', name='%s')>" % (self.id, self.name)
