#!/usr/bin/python3
""" creates a square class with its size
"""


class Square:
        """class Square beginnig
        """
        def __init__(self, size=0):
            """initialization of Square size.
            Args:
            size: the size of the squaresquare size.
            """
            if type(size) == int:
                if size < 0:
                        raise ValueError('size must be >= 0')
                else:
                        self.__size = size
            else:
                raise TypeError('size must be an integer')
