#!/usr/bin/python3
"""
returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    args: my_obj= the object to represent in JSON
    """
    ret = json.dumps(my_obj)
    return ret
