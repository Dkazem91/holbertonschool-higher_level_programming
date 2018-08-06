#!/usr/bin/python3
# requests use
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        qVar = argv[1]
    else:
        qVar = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': qVar})
    try:
        if r.json():
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
