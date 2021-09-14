#!/usr/bin/node
/* use request for get requests */
const request = require('request');

/* set variables */
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

/* format request (url, function) */

request.get(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
