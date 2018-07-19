#!/usr/bin/python3
# sql alchemy awesome
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    # creates city
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
