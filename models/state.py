#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Getter attribute for cities"""
            city_l = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
