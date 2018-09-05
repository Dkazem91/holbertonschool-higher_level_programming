#!/usr/bin/node

let file = process.argv[2];
let string = process.argv[3];
let fs = require('fs');
fs.writeFile(file, string, function (err) {
  if (err) {
    console.log(err);
  }
});
