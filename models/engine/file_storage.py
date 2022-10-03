#!/usr/bin/python3
"""module for file storage"""
import json
import os


class FileStorage:
    """creating class for database engine"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            # self.__objects.update({
            #     type(obj).__name__ + '.' + obj.id: obj.to_dict()
            #     })
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # with open(self.__file_path, 'w') as f:
        #     f.write(json.dumps({key: value.to_dict()
        #                         for key, value in self.__objects.items()}
        #                        ))
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        try:
            # if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
                # json_dict = json.load(f)
            # self.__objects.update(json_dict)
        except:
            pass
