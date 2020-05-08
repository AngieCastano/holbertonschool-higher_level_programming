#!/usr/bin/python3
def best_score(a_dictionary):
    from functools import reduce as f
    if a_dictionary:
        return f(lambda a, b: a if (a > b) else b, a_dictionary.values())
    return None
