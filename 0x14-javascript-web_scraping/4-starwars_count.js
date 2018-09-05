#!/usr/bin/node
const request = require('request');
const address = process.argv[2];
const achil = 'https://swapi.co/api/people/18/';

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).results;
    let count = 0;
    for (let i in results) {
      for (let chr of results[i].characters) {
        if (chr === achil) { count += 1; }
      }
    }
    console.log(count);
  }
});
