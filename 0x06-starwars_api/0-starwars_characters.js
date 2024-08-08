#!/usr/bin/node
const request = require('request');
// Get the Movie ID from command line arguments
const movieId = process.argv[2];

const swapiUrl = `https:
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
