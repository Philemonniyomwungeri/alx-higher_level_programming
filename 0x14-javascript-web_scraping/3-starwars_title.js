#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
if (error) {
 console.error('error:', error);
 } else if (response.statusCode !== 200) {
console.log(`Error: ${response.statusCode}`);
} else {
const movie = JSON.parse(body);
console.log(movie.title);
}
});
