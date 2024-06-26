#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print() {
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i += 1) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;

