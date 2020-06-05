#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance of the
specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    args: obj = object to look, a_class = instance expected object class
    """
    return isinstance(obj, a_class)
