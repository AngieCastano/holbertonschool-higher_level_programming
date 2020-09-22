#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const MatechedArray = list.filter(el => el === searchElement);
  return (MatechedArray.length);
}
;
