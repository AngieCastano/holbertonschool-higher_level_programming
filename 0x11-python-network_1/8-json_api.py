#!/usr/bin/python3
"""
Post of a letter to http://0.0.0.0:5000/search_user
"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        x = requests.post(url, data={"q": ""})
    else:
        x = requests.post(url, data={"q": sys.argv[1]})
    if x.status_code < 400:
        if not isinstance(x.json(), dict):
            print("Not a valid JSON")
        elif bool(x.json()):
            print("[{}] {}".format(x.json().get('id'), x.json().get('name')))
        else:
            print("No result")
    else:
        print("Error code: {}".format(x.status_code))
