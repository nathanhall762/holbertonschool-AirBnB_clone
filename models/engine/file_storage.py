#!/usr/bin/python3
"""module for file storage"""
import json
from models.base_model import BaseModel


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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
        #                         for key, value in self.__objects.items()},
        #                        ))
        # json_objects = {}
        # for key, value in self.__objects.items():
        #     json_objects[key] = value.to_dict()
        # with open(self.__file_path, 'w') as f:
        #     f.write(json.dumps(json_objects))
        with open(self.__file_path, 'w') as f:
            json.dump(
                {
                    k: (v.to_dict() if not isinstance(v, dict) else v)
                    for (k, v) in self.__objects.items()
                }, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        try:
            # if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
                # json_dict = json.load(f)
            # self.__objects.update(json_dict)
        except:
            pass
