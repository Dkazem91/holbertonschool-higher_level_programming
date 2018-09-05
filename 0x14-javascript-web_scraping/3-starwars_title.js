#!/usr/bin/node
let request = require('request');
let num = process.argv[2];
request('http://swapi.co/api/films/' + num, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body)['title']);
  }
});
