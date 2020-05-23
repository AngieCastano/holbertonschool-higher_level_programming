#!/usr/bin/python3
"""
This modul adds 2 integers or floats and returns an int as result


"""


def add_integer(a, b=98):
    """ This function only adds float or integers
    args: a: first number to add, b: second number. types(int, float)
    """
    types = [int, float]
    if type(a) not in types:
        raise TypeError("a must be an integer")

    if type(b) not in types:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
