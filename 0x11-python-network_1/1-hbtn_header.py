#!/usr/bin/python3
# fetches website
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    content = response.info()
    print(content.get('X-Request-Id'))
