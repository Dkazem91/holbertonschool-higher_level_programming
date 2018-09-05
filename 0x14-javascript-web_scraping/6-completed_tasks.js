#!/usr/bin/node
const request = require('request');
const address = process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = {};
    for (let td of JSON.parse(body)) {
      if (td.completed) {
        if (results[td['userId']] === undefined) { results[td['userId']] = 0; }
        results[td['userId']] += 1;
      }
    }
    console.log(results);
  }
});
