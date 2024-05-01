#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import city
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state",
                          cascade="all, delete, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns the list of City instances with state_id
            equals to the current State.id"""
            filtered_cities = []
            from models import storage
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    filtered_cities.append(value)
            return filtered_cities
