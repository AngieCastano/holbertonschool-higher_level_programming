#!/usr/bin/python3
"""
Posting information to an url
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    kwargs = {'email': sys.argv[2]}
    try:
        x = requests.post(url, data=kwargs)
        print(x.text)
    except:
        pass
