#!/usr/bin/node
const LastSquare = require('./5-square');
class Square extends LastSquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    if (this.width > 0 && this.height > 0) {
      const StringWidth = c.repeat(this.width) + '\n';
      const StringHeight = StringWidth.repeat(this.height);
      console.log(StringHeight.slice(0, -1));
    }
  }
}
module.exports = Square;
