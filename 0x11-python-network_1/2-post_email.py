#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response.
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    # get the data from the web page
    ses_url = sys.argv[1]
    ses_email = sys.argv[2]
    # get the headers and convert it in text for parse
    data = urllib.parse.urlencode({'email': ses_email}).encode('ascii')
    # save the new email in a new request and upload the request to the page
    req = urllib.request.Request(ses_url, data)
    # get the response for the request
    with urllib.request.urlopen(req) as response:
        resp = response.read()
    # print the response coded for utf-8
    print(resp.decode('utf-8'))
