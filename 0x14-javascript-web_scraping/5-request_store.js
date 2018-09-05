#!/usr/bin/node
let request = require('request');
let address = process.argv[2];
request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let fs = require('fs');
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) { console.log(err); }
    });
  }
});
