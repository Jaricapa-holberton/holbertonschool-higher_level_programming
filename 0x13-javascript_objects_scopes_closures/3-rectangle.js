#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    const char = 'X';
    let printline;
    const dimension = this.height;
    for (i = 1; i <= dimension; i++) {
      if (i === 1 || i === dimension) {
        printline = Array(dimension + 1).join(char);
      }
      console.log(printline);
    }
  }
};
