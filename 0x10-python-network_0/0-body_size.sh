#!/bin/bash
# Displays the size of the body content of indicated URL. go to the url direction, search for content and bring just the count
curl -sI "$1" | grep -i "Content-Length:" | cut -d " " -f2
