#!/bin/bash
# Script that do a POST request and sent two values/variables.
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -sX POST "$1"
