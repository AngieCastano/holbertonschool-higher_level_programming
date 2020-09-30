#!/usr/bin/python3
"""
Post to http://0.0.0.0:5000/search_user
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]

        url = 'http://0.0.0.0:5000/search_user'

        r = requests.post(url, data={'q': q})

        try:
            response = r.json()
            print("[{}] {}".format(response['id'], response['name']))
        except Exception:
            print('Not a valid JSON')

    elif len(sys.argv) == 1:
        print('No result')
