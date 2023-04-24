#!/usr/bin/python3
""" City module for AirBnB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """ City object: Inherits from BaseModel and Base (sqlalchemy) """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place",
            backref=backref("cities", cascade="all,delete"),
            cascade="all, delete, delete-orphan",
            passive_deletes=True,
            single_parent=True)
