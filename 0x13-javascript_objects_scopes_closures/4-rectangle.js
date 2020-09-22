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

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const Temp = this.width;
    this.width = this.height;
    this.height = Temp;
  }
}
module.exports = Rectangle;
