#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
if (process.argv[2] == 'https://swapi-api.hbtn.io/api/films/'){
  request(url, function (error, response) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(response.body).films.length);
  });
}
