#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object:
"""


def lookup(obj):
    """
    args:  obj= object to know it's methods and attributes
    """
    return dir(obj)
