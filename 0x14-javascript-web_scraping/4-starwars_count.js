#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = 18;

request(apiUrl, function (error, response, body) {
	  if (error) {
		      console.error('error:', error);
	  } else if (response.statusCode !== 200) {
			        console.error(`Error: ${response.statusCode}`);
		    } else {
const films = JSON.parse(body).results;
let count = 0;

films.forEach(film => {
if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
 count++;
}
});

console.log(count);
}
});
