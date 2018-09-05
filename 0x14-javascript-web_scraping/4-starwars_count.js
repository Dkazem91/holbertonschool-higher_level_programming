#!/usr/bin/node
const request = require('request');
const address = process.argv[2];
let achil = 'https://swapi.co/api/people/18/';


request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body)['results'];
    let count = 0;
    for (let i in results) {
      if (results[i]['characters'].indexOf(achil) >= 0) {count += 1;}
    }
    console.log(count);
  }
});
