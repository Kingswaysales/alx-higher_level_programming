#!/usr/bin/python3
"""
    Use package requests to fetch https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
