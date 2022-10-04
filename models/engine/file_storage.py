#!/usr/bin/python3
"""module for file storage"""
import json
import models


class FileStorage:
    """creating class for database engine"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects.update(
            {f"{type(obj).__name__}.{obj.id}": obj
             })

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            zach = {}
            for key, value in self.__objects.items():
                zach.update({key: value.to_dict()})
            f.write(json.dumps(zach))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                zach = json.loads(f.read())
                for key, value in zach.items():
                    self.__objects[key] = models.BaseModel(**value)
        except:
            pass
