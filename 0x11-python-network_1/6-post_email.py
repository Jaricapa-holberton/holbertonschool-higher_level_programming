#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response.
"""
if __name__ == "__main__":
    import requests
    import sys

    # get the data from the web page
    ses_url = sys.argv[1]
    ses_email = sys.argv[2]
    # upload the email on the url modifing the headers
    # NOTESS: try hodor changing the user_agent key with the data parameter
    resp = requests.post(s_url, data={'email': ses_email})
    # print the response coded for utf-8
    print(resp.text)
