#!/usr/bin/python3
"""This module defines a base class for all models in our HBNB clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models
from models import storage
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all HBNB models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid.uuid4())
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = kwargs.get
                ('created_at', datetime.utcnow())

            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.utcnow()

            if isinstance(kwargs.get('updated_at'), str):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')

            if isinstance(kwargs.get('created_at'), str):
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                        '%Y-%m-%dT%H:%M:%S.%f')

            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict = self.__dict__.copy()
        if "_sa_instance_state" in dict:
            dict.pop("_sa_instance_state")
        return '[{}] ({}) {}'.format(cls, self.id, dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            dictionary.pop("_sa_instance_state")

        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete()
