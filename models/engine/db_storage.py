#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
import os
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage():
    """A DBStorage class"""
    __engine = None
    __session = None

    classes = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        """Instantiates the DBStorage class"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        url = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session to retrieve
        objects depending on the class name (argument cls)"""
        class_dict = {}
        if cls is not None:
            if cls in self.classes:
                query = self.__session.query(cls).all()
                for row in query:
                    key = "{}.{}".format(cls.__name__, row.id)
                    class_dict[key] = row
        else:
            for cls in self.classes:
                query = self.__session.query(cls).all()
                for row in query:
                    key = "{}.{}".format(cls.__name__, row.id)
                    class_dict[key] = row
        return class_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database into the current session"""
        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create the current database session
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the database session."""
        self.__session.remove()
