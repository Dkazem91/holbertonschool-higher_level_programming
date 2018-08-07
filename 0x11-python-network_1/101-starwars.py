#!/usr/bin/python3
# requests use
import requests
from sys import argv


def paginate(address):
    if address is None:
        return
    r = requests.get(address).json()
    for dik in r.get('results'):
        print(dik.get('name'))
    return paginate(r.get('next'))


if __name__ == "__main__":
    r = requests.get("https://swapi.co/api/").json().get('people')
    idsite = "{}?search={}".format(r, argv[1])
    section = requests.get(idsite).json()
    print("Number of results: {}".format(section.get('count')))
    for dik in section.get('results'):
        print(dik.get('name'))
    paginate(section.get('next'))
