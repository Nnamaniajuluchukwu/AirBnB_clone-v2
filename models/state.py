#!/usr/bin/python3
""" State module for AirBnB Clone Project"""
""" Importing necessary modules. """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
	"""" State Object: inherit from BaseModel and Base (sqlalchemy)"""
	__tablename__ = "states"
	name = Column(String(128), nullable=False)
	cities = relationship("City", backref=backref("state", cascade="all,delete"),
                        cascade="all, delete, delete-orphan",
                        passive_deletes=True,
                        single_parent=True)

	if getenv("HBNB_TYPE_STORAGE") != "db":
		@property
		def cities(self):
			""" Return list of city instances with state.id. """
			from models import storage
			from models.city import City
			cities_ = [obj for obj in storage.all(City).values()
                	 if obj.state_id == self.id]
			return cities_