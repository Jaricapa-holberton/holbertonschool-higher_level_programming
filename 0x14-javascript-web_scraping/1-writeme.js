#!/usr/bin/node
/* use fs for write files */
const fs = require('fs');

/* format fs.writeFile( Path, Data, Callback) */

/* set variables */
const filename = process.argv[2];
const string = process.argv[3];

/* execute reading */
fs.writeFile(filename, string, function (err) {
  if (err) {
    console.log(err);
  }
});
