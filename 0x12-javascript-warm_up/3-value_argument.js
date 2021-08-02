#!/usr/bin/node
const myArgs = process.argv.slice(2);
const numArgs = myArgs.length;
if (numArgs === 0) {
  console.log('No argument');
} else {
  let idx;
  for (idx = 0; idx < numArgs; idx++) {
    console.log(myArgs[idx]);
  }
}
