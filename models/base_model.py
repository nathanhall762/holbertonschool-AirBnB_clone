#!/usr/bin/python3
""" Base Model Class """
from datetime import *
import uuid


class BaseModel:
    """ Base Class """
    def __init__(self):
        # Public instance attributes:
        # id: string - assign with an uuid when an instance is created:
            # you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
            # the goal is to have unique id for each BaseModel
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
        # created_at: datetime - assign with the current datetime when an instance is created
        # updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object

    # __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    def __str__(self):
        return "[{}] ({}) <{}>".format(__name__, self.id, self.__dict__)

# Public instance methods:
    # save(self): updates the public instance attribute updated_at with the current datetime
    def save(self):
        """ sets updated_at to current datetime """
        self.updated_at = datetime.now().isoformat()

    # to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
    def to_dict(self):
        """ returns a dictionary containing all keys/values"""
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

        # by using self.__dict__, only instance attributes set will be returned
        # a key __class__ must be added to this dictionary with the class name of the object
        # created_at and updated_at must be converted to string object in ISO format:
            # format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            # you can use isoformat() of datetime object
        # This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
