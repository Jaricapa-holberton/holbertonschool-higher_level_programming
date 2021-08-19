#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
# Displays the size of the body content of indicated URL.
# go to the url direction, search for content and bring just the count
curl -sI "$1" | grep Content-Length | cut -d" " -f2 