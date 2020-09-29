#!/usr/bin/python3
"""
Github API
"""
import requests
import sys

if __name__ == '__main__':
    import requests
    import sys
    tok = sys.argv[2]
    h = {'Authorization': 'token ' + tok}
    login = requests.get('https://api.github.com/user', headers=h)
    print(login.json().get('id'))
