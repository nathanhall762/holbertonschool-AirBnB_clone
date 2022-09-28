#!/usr/bin/python3
""" Base Model Class """
from datetime import *
import uuid


class BaseModel:
    """ Base Class """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.save()

    def __str__(self):
        return "[{}] ({}) <{}>".format(__name__, self.id, self.__dict__)

    def save(self):
        """ sets updated_at to current datetime """

        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """ returns a dictionary containing all keys/values"""

        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
