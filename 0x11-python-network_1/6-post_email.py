#!/usr/bin/python3
"""
Posting information to an url
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    x = requests.post(url, data={'email': sys.argv[2]})
    print(x.text)
