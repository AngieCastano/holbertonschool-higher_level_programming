#!/usr/bin/python3
"""
Getting information about the holberton page
"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    for key in html:
        print("\t-{}".format(key))
