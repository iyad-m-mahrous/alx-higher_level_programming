#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((list, current) => {
    list.push(current);
    return list;
  }, []);
};
