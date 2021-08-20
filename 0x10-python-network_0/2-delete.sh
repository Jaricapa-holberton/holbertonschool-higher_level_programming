#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response
# Script that sends a DELETE request.
curl -sX DELETE "$1"