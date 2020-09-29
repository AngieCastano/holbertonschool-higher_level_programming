#!/usr/bin/python3
"""
Getting information about the holberton page with request
"""

if __name__ == '__main__':
        import requests

        x = requests.get('https://intranet.hbtn.io/status')
        print("Body response:")
        print("\t- type: {}".format(type(x.text)))
        print("\t- content: {}".format(x.text))
