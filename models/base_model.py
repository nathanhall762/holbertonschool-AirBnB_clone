#!/usr/bin/python3
""" Base Model Class """
from datetime import datetime
import uuid
import models


class BaseModel:
    """ Base Class for HolBnB project """

    def __init__(self, *args, **kwargs):
        """instantiates base class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
<<<<<<< HEAD
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id,
                                       self.__dict__)
=======
        """overwriting ___str__ builtin"""
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id,
                                     self.__dict__)
>>>>>>> master

    def save(self):
        """ sets updated_at to current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values"""
        class_dict = self.__dict__.copy()
        class_dict['__class__'] = self.__class__.__name__
        class_dict['created_at'] = self.created_at.isoformat()
        class_dict['updated_at'] = self.updated_at.isoformat()
        return class_dict
