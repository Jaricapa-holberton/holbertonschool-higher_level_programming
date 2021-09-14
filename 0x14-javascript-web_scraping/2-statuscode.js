#!/usr/bin/node
/* use request for get requests */
const request = require('request');

/* format request (url, function) */

request.get(process.argv[2], function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code: ' + response.statusCode);
});
