#!/usr/bin/node
/* use fs for read files */
const fs = require('fs');

/* format fs.readFile( filename, encoding, callback_function ) */

/* set variables */
const filename = process.argv[2];
const encoding = 'utf8';

/* execute reading */
fs.readFile(filename, encoding, function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
