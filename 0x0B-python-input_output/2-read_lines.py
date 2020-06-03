#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        for counter, line in enumerate(myFile, 1):
            pass
        myFile.seek(0)
        if nb_lines < 1 or nb_lines >= counter:
            print(myFile.read(), end="")
        else:
            for counter, line in enumerate(myFile, 1):
                if counter > nb_lines:
                    break
                print(myFile.readline(), end="")
