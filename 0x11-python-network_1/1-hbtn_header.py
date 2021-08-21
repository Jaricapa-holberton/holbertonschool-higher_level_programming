#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the
response.
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    # get the data from the web page
    ses_url = sys.argv[1]
    with urllib.request.urlopen(ses_url) as response:
        # save the header
        header = response.headers
    # print the value of the key 'X-Request-Id'
    print(header.get('X-Request-Id'))
