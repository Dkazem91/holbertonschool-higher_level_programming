#!/usr/bin/node
const request = require('request');
const address = 'https://swapi.co/api/films/' + process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).characters;
    let promises = [];
    for (let i of results) {
      let thing = new Promise(function (resolve, reject) {
        request(i, (e, r, b) => resolve(JSON.parse(b)['name']));
      });
      promises.push(thing);
    }
    Promise.all(promises).then((a) => {
      for (let i of a) {
        console.log(i);
      }
    });
  }
});
