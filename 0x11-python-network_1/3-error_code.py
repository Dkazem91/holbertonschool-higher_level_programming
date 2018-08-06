#!/usr/bin/python3
# posts email
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            thisPage = response.read().decode('utf-8')
            print(thisPage)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
