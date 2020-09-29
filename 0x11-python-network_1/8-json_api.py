#!/usr/bin/python3
'''
Post to http://0.0.0.0:5000/search_user API
'''
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('No result')
        exit()
    if len(sys.argv) == 2:
        q = sys.argv[1]
        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, data={'q': q})
        try:
            json = r.json()
            print("[{}] {}".format(json.get('id'),
                                   json.get('name')))
        except ValueError:
            print('Not a valid JSON')
