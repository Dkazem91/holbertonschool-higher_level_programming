#!/usr/bin/node
let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
