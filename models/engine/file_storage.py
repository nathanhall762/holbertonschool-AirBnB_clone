#!/usr/bin/python3
"""module for file storage"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects.update({type(obj).__name__ + obj.id: obj})
        # need to fix the id format given here

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path) as f:
                self.__objects = json.loads(f.read())
        except:
            pass
