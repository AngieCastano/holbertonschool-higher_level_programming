#/usr/bin/python3
import inspect
from models.base import Base
"""
Class Rectangle. inherits from Class base
"""


def type_error(value, name):
    """
    Validates value type
    """
    types = [int]
    if type(value) not in types:
        raise ValueError("{} must be an integer".format(name))

def positive_number(value, name):
    """
    Validates thet value is a positive number
    """
    if value < 1:
        raise ValueError("{} must be > 0".format(name))

def negative_number(value, name):
    """
    Validates that value is not a negative number
    """
    if value < 0:
        raise ValueError("{} must be >= 0".format(name))

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
        type_error(width, "width")
        positive_number(width, "width")
        self.__width = width
        type_error(height, "height")
        positive_number(height, "height")
        self.__height = height
        type_error(x , "x")
        negative_number(x ,"x")
        self.__x = x
        type_error(y , "y")
        negative_number(y , "y")
        self.__y = y

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
        print("width setter called")
        type_error(value, "width")
        positive_number(value, "width")
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
        print("heigth setter called")
        type_error(value, "height")
        positive_number(value, "height")
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
        print("x setter called")
        type_error(value, "x")
        negative_number(value, "x")
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
        print("y setter called")
        type_error(value, "y")
        negative_number(value, "y")
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
        print("\n" * self.__y, end = "")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#"* self.__width)

    def __str__(self):
        """
        modificating the __str__magic method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the object values with args
        """
        if args is not None:
            for arg_int, ar in zip(self.__dict__.keys(), args):
                if hasattr(self, arg_int):
                    setattr(self, arg_int, ar)
        if kwargs is not None:
            for k in kwargs:
                if hasattr(self, k):
                    setattr(self, k, kwargs[k])
