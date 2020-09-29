#!/usr/bin/python3
"""
Posting information to an url
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    x = requests.post(url, data={'email': sys.argv[2]})
    print(x.text)
