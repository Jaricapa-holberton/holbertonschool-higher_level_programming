#!/usr/bin/node

/* use fs and requests */
const fs = require('fs');
const request = require('request');

/* set variables */
const url = process.argv[2];
const destiny = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  fs.writeFile(destiny, body, error => {
    if (error) console.log(error);
  });
});
