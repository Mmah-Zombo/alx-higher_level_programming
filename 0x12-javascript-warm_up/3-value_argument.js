#!/usr/bin/node

const [arg] = process.argv.slice(2);

if (arg) {
  console.log(arg);
} else {
  console.log("No argument");
}
