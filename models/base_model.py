#!/usr/bin/python3
"""BaseModel class"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base object for all common attributes:
    attr1: id 
    attr: created_at
    attr3: updated_at
    """

    def __init__(self,*args, **kwargs):
        """Initializes instance attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            if kwargs is not None:
                for key, value in kwargs.item():
                    if (key == "created_at" or key == "updated_at"):
                        if (type(value) == str):
                            new_object = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'
                            )
                            self.__dict__[key] = new_object
                    else:
                        self.__dict__[key] = value

    def __str__(self):
        """ prints the str rep of [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)


    def save(self):
        """Updated public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        return new_dict
