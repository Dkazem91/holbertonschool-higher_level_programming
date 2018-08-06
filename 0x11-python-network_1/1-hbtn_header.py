#!/usr/bin/python3
# fetches website
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
