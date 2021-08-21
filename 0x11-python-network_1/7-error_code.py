#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a request
to the passed URL and displays the body of the response.
Manage urllib.error.HTTPError exceptions
"""
if __name__ == "__main__":
    import sys
    import requests

    # get the data from the web page
    ses_url = sys.argv[1]
    # save the url in a new request and upload the request to the page
    req = requests.get(ses_url)
    # print the body of the page except if fails
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
