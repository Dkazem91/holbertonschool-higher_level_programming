#!/usr/bin/node
let request = require('request');
let address = 'https://swapi.co/api/people/?search=Wedge Antilles';
request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body)['results'][0]['films'].length);
  }
});
