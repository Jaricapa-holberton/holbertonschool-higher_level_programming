#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    /* if (size > 0) {
      this.size = size;
    } */
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        console.log(('X'.repeat(this.width)));
      } else {
        console.log((c.repeat(this.width)));
      }
    }
  }
};
