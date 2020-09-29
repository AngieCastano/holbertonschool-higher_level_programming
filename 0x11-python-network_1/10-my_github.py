#!/usr/bin/python3
"""
Github API
"""
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}"
    x = requests.get(url)
    print(x.json().get('id'))
