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
        """Initializes instance"""
        self.id = str(uuid4())
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """ prints the str rep of [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updated public instance"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary"""
        return new_dict

