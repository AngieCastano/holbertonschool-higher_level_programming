#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      const StringWidth = 'X'.repeat(this.width) + '\n';
      const StringHeight = StringWidth.repeat(this.height);
      console.log(StringHeight.slice(0, -1));
    }
  }
}
module.exports = Rectangle;
