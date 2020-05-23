#!/usr/bin/python3
"""Modules that prints a square of size size



"""


def print_square(size):
    """
    function that prints a square of size size. size= square's size
    """
    types = [int]
    if type(size) not in types:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size * "#")
