#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a request
to the passed URL and displays the body of the response.
Manage urllib.error.HTTPError exceptions
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

    # get the data from the web page
    ses_url = sys.argv[1]
    # save the url in a new request and upload the request to the page
    req = urllib.request.Request(ses_url)
    # print the body of the page except if fails
    try:
        with urllib.request.urlopen(req) as response:
            resp = response.read()
        print(resp.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
