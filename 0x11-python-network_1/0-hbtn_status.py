#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

import urllib.request

# get the data from the web page
ses_url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(ses_url) as response:
    # save the html code fetched
    html = response.read()
# print the text as main demands
print(html)
print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html.decode('utf8')))
