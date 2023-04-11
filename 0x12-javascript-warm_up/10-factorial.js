#!/usr/bin/node
function factorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const { argv } = require('process');
const num = Number(argv[2]);

console.log(factorial(num));
