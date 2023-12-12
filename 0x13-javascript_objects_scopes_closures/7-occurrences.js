#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => {
    return current === searchElement ? count++ : count;
  }, 0);
};
