#!/usr/bin/python3
"""
Send a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    # set varible empty for check changes
    letter = ""
    ses_url = "http://0.0.0.0:5000/search_user"
    # if arg was given change the letter value
    if (len(sys.argv) > 1):
        letter = sys.argv[1]
    # get the info about the url and upload info about letter
    req = requests.post(ses_url, data={'q': letter})
    # get the header of the url
    req_type = req.headers['Content-Type']
    # check if the header is a json type
    if (req_type == 'application/json'):
        # as json type, serialize to json
        req_json = req.json()
        # if its empty stop, if not, show data from json
        if req_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(req_json['id'], req_json['name']))
    else:
        print("Not a valid JSON")
