#!/usr/bin/python3
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
import json
import os

class FileStorage:
    """A class wit the attributes:
    attri1(__file_path): JSON file
    attr2(__objects): dictionary
    """
    __file_path = "file.json"
    open(__file_path, "a")
    __objects = {}
    
    def all(self):
        """Returns a dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__dict__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Selializes __objects to JSON file"""
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, mode="w") as my_file:
            json.dumb(dict, my_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the __file_path exists)
        """
        my_class = {"BaseModel": BaseModel,
                    "City": City, "Place": Place, "Review": Review,
                    "User": User, "State": State}
        dic_to_fill = {}
        if(os.stat(self.__file_path).st_size != 0):
            with open(self.__file_path) as json_file:
                dict_to_fill = json.load(json_file)
                for key, value in dic_to_fill.items():
                    self.__objects[key] = my_class[value['__class__']](**value)
