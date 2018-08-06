#!/usr/bin/python3
# requests use
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get("https://swapi.co/api/").json().get('people')
    idsite = "{}?search={}".format(r, argv[1])
    section = requests.get(idsite).json()
    print("Number of results: {}".format(section.get('count')))
    for dik in section.get('results'):
        print(dik.get('name'))
