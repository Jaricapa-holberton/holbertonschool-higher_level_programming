#!/bin/bash
# Display all HTTP methods the server will accept.
curl -o /dev/null -s -w "%{http_code}" "$1"