#!/usr/bin/python3
"""storage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ storage Object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ holder """
        return __objects

    def new(self, obj):
        """ holder """
        __objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ holder """
        dic = {}
        for key, value in __objects.items():
            dic[key] = value.to_dict()
        with open(__file_path, 'w') as f:
            json.dump(dic, f)
        f.close()

    def reload(self):
        """ holder """
        idclasses = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
        data = {}
        if(os.stat(__file_path).st_size is not 0):
            with open(__file_path) as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    __objects[key] =\
                        idclasses[value['__class__']](**value)
