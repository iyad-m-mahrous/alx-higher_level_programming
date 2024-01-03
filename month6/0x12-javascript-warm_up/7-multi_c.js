#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < Number(process.argv[2]); count++) {
    console.log('C is fun');
  }
}
