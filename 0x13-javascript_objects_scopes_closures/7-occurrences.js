#!/usr/local/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((val) => val == searchElement).length;
};
