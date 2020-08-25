#!/usr/bin/python3
''' script that sends a POST request '''

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url, data) as response:
        html = response.read().decode('utf-8')
        print(html)
