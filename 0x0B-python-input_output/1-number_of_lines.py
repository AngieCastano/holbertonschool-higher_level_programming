#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        for counter, line in enumerate(myFile, 1):
            pass
        return counter
