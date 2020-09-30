#!/usr/bin/python3
"""
Github API
"""
import requests
import sys


if __name__ == '__main__':
    import requests
    import sys
    rep_n = sys.argv[1]
    owner_n = sys.argv[2]
    u = requests.get(f'https://api.github.com/repos/{owner_n}/{rep_n}/commits')
    dictionary = u.json()
    for item in dictionary[0:10]:
        print(item.get('sha'), item.get('author').get('login'))
