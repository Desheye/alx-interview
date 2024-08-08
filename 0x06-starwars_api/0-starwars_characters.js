#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Construct the SWAPI URL for the movie
const swapiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the HTTP request
request(swapiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Print character names
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (!charError && charResponse.statusCode === 200) {
        const character = JSON.parse(charBody);
        console.log(character.name);
      }
    });
  });
});

