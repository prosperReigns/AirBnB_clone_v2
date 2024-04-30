#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlclchemy import String, Colunm, Foriegnkey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")
    places = relationship("Place", back_populates="city",
                          cascade="all, delete, delete-orphan")
