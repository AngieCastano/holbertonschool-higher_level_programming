#!/bin/python3
""" This module is about says a person's name



"""


def say_my_name(first_name, last_name=""):
    """function that prints sombody's name
    first_name = person's first name. last_name = person's last name
    """
    types = [str]
    if type(first_name) not in types:
        raise TypeError("first_name must be a string")
    if type(last_name) not in types:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
