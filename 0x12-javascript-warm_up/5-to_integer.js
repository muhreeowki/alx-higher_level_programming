#!/usr/bin/node
const argv = process.argv;
const number = Number(argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
}
console.log(number);
