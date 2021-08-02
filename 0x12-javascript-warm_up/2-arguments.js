#!/usr/bin/node
const myArgs = process.argv.slice(2);
const numArgs = myArgs.length;
if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
