#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests

    # get the data from the web page
    req = requests.get('https://intranet.hbtn.io/status').text
    # print the text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
