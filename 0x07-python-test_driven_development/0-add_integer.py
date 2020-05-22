#!/usr/bin/python3
def add_integer(a, b=98):
    """ This function only adds float or integers"""
    types = [int, float]
    try:
        if type(a) not in types:
            raise TypeError
    except TypeError:
        return "a must be an integer"
    try:
        if type(b) not in types:
            raise TypeError
    except TypeError:
        return "b must be an integer"
    else:
        return int(a) + int(b)
