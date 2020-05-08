#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    if isinstance(roman_string, str):
        if roman_string:
            n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                 "D": 500, "M": 1000}
            to_sum = [n[letter] for letter in roman_string]
            return reduce(lambda x, y: x+y, to_sum)
        return 0
    return 0
