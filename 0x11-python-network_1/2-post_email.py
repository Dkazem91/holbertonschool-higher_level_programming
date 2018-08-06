#!/usr/bin/python3
# posts email
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = bytes(urllib.parse.urlencode(data).encode())
    handler = urllib.request.urlopen(sys.argv[1], data)
    with urllib.request.urlopen(handler) as response:
        print(response.read().decode('utf-8'))
