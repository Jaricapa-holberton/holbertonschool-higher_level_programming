#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    import requests
    import sys

    # get the credentials
    repository = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repository)
    # acess to the url and get the list of commits
    req = requests.get(url)
    commits = req.json()
    # order by most recent to oldest
    for i in range(10):
        commit = commits[i]
        ses_sha = commit.get('sha')
        ses_author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(ses_sha, ses_author))
