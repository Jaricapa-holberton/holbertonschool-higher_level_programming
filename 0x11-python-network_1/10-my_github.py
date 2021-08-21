#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests

    # get the credentials
    ses_user = sys.argv[1]
    ses_passw = sys.argv[2]
    s_url = 'https://api.github.com/user'
    # get the data from github via API
    req = requests.get(s_url, auth=(ses_user, ses_passw))
    # save the items from the json object and search for the id
    req_id = req.json().get('id')
    print(req_id)
