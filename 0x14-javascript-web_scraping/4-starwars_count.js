#!/usr/bin/node
/* use request for get requests */
const request = require('request');

/* set variables */
const url = process.argv[2];
let nFilms = 0;

/* format request (url, function) */

request.get(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const films = JSON.parse(body).results;
  for (const film of films) {
    const characters = film.characters;
    if (characters.find((c) => c.endsWith('/18/'))) {
      nFilms += 1;
    }
  }
  console.log(nFilms);
});
