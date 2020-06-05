#!/usr/bin/python3
"""
Write an empty class BaseGeometry
"""


class BaseGeometry:
    """
    empty class BaseGeometry
    """
    def area(self):
        """
        args: self = instance
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value type
        """
        types = [int]
        if type(value) not in types:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
