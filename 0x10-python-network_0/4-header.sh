#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
# Script that set a Header variable and do a GET request.
curl -sH "X-HolbertonSchool-User-Id:98" "$1"