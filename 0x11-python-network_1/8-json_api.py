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
    try:
        if bool(x.json()):
            print("{} {}".format(x.json().get('id'), x.json().get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
