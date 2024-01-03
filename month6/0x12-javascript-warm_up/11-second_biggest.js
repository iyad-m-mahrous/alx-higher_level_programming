#!/usr/bin/node
const newArray = process.argv.slice(2).map(Number).sort((a, b) => b - a);
newArray[1] ? console.log(newArray[1]) : console.log(0);
