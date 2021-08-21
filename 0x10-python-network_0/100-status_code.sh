#!/bin/bash
# Script that do a request and display the status code of the response.
curl -o /dev/null -s -w "%{http_code}" "$1"