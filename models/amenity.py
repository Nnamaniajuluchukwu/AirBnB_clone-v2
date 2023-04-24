#!/usr/bin/python3
""" Amenity Module for AirBnB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity object: Inherits from BaseModel and Base (sqlalchemy) """
#    __tablename__ = "amenities"
#    name = Column(String(128), nullable=False)
#   place_amenities = relationship("Place", secondary="place_amenity",
#            viewonly=False, back_populates="amenities")
