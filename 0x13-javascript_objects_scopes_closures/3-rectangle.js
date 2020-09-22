#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (var j = 0; j < this.height; j++) {
      for (var i = 0; i < this.width; i++) {
        process.stdout.write('x');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Rectangle;
