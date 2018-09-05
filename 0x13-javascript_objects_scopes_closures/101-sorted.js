#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newdict = {};
for (let key in dict) {
  if (newdict[dict[key]] === undefined) {
    newdict[dict[key]] = [key];
  } else {
    newdict[dict[key]].push(key);
  }
}
console.log(newdict);
