#!/usr/bin/node

const request = require('request');

const SWAPI_BASE_URL = 'https://swapi.dev/api';

function getMovieCharacters (movieId) {
  const filmEndpoint = `${SWAPI_BASE_URL}/films/${movieId}/`;

  request(filmEndpoint, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status Code:', response.statusCode);
    } else {
      const characters = body.characters;
      printCharacters(characters, 0);
    }
  });
}

function printCharacters (characters, index) {
  if (index < characters.length) {
    const characterEndpoint = characters[index];
    request(characterEndpoint, { json: true }, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        console.log(body.name);
        printCharacters(characters, index + 1);
      } else {
        console.error('Error fetching character:', error);
      }
    });
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
} else {
  getMovieCharacters(movieId);
}
