#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the
response.
"""
if __name__ == "__main__":
    import requests
    import sys

    # get the data from the web page
    ses_url = sys.argv[1]
    req = requests.get(ses_url)
    # save the header
    head = req.headers.get('X-Request-Id')
    # print the value of the key 'X-Request-Id'
    print(head)
