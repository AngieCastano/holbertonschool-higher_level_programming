#!/usr/bin/python3
from models.base import Base


"""
Class Rectangle. inherits from Class base
"""


class Rectangle(Base):
    """
    inherits from rhe Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        args: width = object's width, height = height's rectangle
        x = horizontal position, y = vertical position, id = object's id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieve's rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width's Rectangle
        """
        types = [int]
        if type(value) not in types:
                    raise ValueError("width must be an integer")
        if value < 1:
                    raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve's the rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height's rectangle
        """
        types = [int]
        if type(value) not in types:
            raise ValueError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieve's x Rectangles position
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x rectangle's position
        """
        types = [int]
        if type(value) not in types:
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieve's the y rectangle's position
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y' Rectangle position
        """
        types = [int]
        if type(value) not in types:
            raise ValueError("y must be an integer")
        if value < 0:
                    raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the rectangle's area
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays rectangle's graphic
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        modificating the __str__magic method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the object values with args
        """
        if args is not None:
            if len(args) > 0:
                for arg_int, ar in zip(self.__dict__.keys(), args[0]):
                    if hasattr(self, arg_int):
                        setattr(self, arg_int, ar)
        if kwargs is not None:
            for k in kwargs:
                if hasattr(self, k):
                    setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """
        Returns an object dictionary
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
