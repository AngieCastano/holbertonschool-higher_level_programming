#!/usr/bin/python3
"""
returns an object (Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    args: my_str = string to convet in a JSON
    """
    return json.loads(my_str)
