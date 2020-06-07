#!/usr/bin/python3
"""
Class Base
"""


class Base:
    """
    base class
    """
    __nb_objects = 0
    __ids = []
    def __init__(self, id=None):
        """
        args: id = object's id
        """
        if id:
            self.id = id
            if self.id not in Base.__ids:
                Base.__ids.append(self.id)
            else:
                raise ValueError("id already exists")
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            if self.id not in Base.__ids:
                Base.__ids.append(self.id)
            else:
                Base.__nb_objects -= 1
                raise ValueError("id already exists")
