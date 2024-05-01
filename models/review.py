#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Colunm, ForiegnKey, String
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")
