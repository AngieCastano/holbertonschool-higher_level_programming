#!/usr/bin/python3
"""
Getting information about the holberton page with request
"""

if __name__ == '__main__':
        import requests
        import sys

        url = sys.argv[1]
        x = requests.get(url)
        print(x.headers.get('X-Request-Id'))
