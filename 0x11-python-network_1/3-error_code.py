#!/usr/bin/python3
"""
Getting information about the holberton page
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as data:
            print(data.info())
    except urllib.error.HTTPError:
        print("Error code: {}".format(urllib.error.HTTPError.getcode()))
