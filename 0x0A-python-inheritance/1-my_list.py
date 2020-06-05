#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """
    inherits from the class list
    """
    def print_sorted(self):
        """
        recives the object list
        """
        new = self[:]
        new.sort()
        print(new)
