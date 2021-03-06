#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    args: my_obj = object, filename
    """
    with open(filename, mode="w") as File:
        File.write(json.dumps(my_obj))
