#!/usr/bin/node
const numOccurrences = Number(process.argv[2]);

if (Number.isNaN(numOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
