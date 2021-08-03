#!/usr/bin/node

let num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (; num > 0; num--) {
    console.log('C is fun');
  }
}
