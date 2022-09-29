#!/usr/bin/python3
""" Base Model Class """
from datetime import *
import uuid
import json


class BaseModel:
    """ Base Class """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) <{}>".format(__name__, self.id, self.__dict__)

    def save(self):
        """ sets updated_at to current datetime """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values"""
        # class_dict = self.__dict__.copy()
        # class_dict['__class__'] = __class__.__name__
        # class_dict['created_at'] = self.created_at.isoformat()
        # class_dict['updated_at'] = self.updated_at.isoformat()
        # return class_dict

        newDict = self.__dict__.copy()
        newDict.pop((
            key for key in dir(self)
            if key.startswith("__") and key.endswith("__")), None)
        newDict['__class__'] = __class__.__name__
        return newDict
