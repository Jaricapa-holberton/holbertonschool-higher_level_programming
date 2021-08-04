#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    if (size > 0) {
      this.size = size;
    }
  }
};
