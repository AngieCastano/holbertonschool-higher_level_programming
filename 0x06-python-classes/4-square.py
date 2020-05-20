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

        def area(self):
            """initialization of Square size.
            Args:
            size: the size of the squaresquare size.
            """
            return (self.__size ** 2)

        @property
        def size(self):
            """
            size method, retrives size
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            size method, sets size
            """
            if type(value) == int:
                    if value < 0:
                        raise ValueError('size must be >= 0')
                    else:
                            self.__size = value
            else:
                    raise TypeError('size must be an integer')
