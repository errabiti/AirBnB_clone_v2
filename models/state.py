""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        @property
        def cities(self):
            """Getter attribute for cities"""
            from models import storage
            city_l = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l

    id = Column(String(60), nullable=False, primary_key=True)
