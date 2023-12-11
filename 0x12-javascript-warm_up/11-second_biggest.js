#!/usr/bin/node
let max = -Infinity;
let max2 = 0;

process.argv.forEach((num) => {
  if (!isNan(num) && Number(num) > max) {
    max !== -Infinity ? max2 = max : max2 = 0;
    max = num;
  }
});

console.log(max2);
