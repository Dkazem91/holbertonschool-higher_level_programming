#!/usr/bin/python3
# fetches website
import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    content = response.info()
    print(content.get('X-Request-Id'))
