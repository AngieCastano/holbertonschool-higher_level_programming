#!/usr/bin/python3
from models.rectangle import Rectangle
"""
Class Square inherits from base
"""


class Square(Rectangle):
    """
    inherint from Rectangle that inherits from Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        args: size = objects width and height
        x = horizontal position, y = vertical position, id = object's id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Doesn't print twice the size
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """
        Retrieves the size square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size/ width square
        """
        self.width = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes with args an kwargs
        """
        new_args = args[:]
        if args:
            if len(args) > 2:
                new_args = args[:]
                new_args = list(new_args)
                new_args.insert(1, args[1])
                new_args = tuple(new_args)
        if kwargs:
            if "size" in kwargs:
                kwargs["width"] = kwargs["size"]
                kwargs["height"] = kwargs["size"]
        super(Square, self).update(new_args, **kwargs)

    def to_dictionary(self):
        """
        Returns the objects dictionary
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
