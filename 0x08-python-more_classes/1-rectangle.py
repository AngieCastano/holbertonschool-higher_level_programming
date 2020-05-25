#!/usr/bin/python3
"""

Module that defines a rectangle with width and heigth

"""


class Rectangle:
    """
    Class Rectangle beginnig
    """
    def __init__(self, width=0, height=0):
        """ Inizialization of class Rectangle
        width = Rectangle width. Heigth = Rectangle Heigth
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Retrieves Rectangle's width
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the Rectangle height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the Rectangle's width
        value = new Rectangle's width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height
        value = Rectangles height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
