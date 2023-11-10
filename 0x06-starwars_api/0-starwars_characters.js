const axios = require('axios');

// Check if the user provided a movie ID as a command-line argument
if (process.argv.length < 3) {
    console.log("Usage: node 0-starwars_characters.js <Movie ID>");
    process.exit(1);
}

// Define the Star Wars API base URL
const baseUrl = "https://swapi.dev/api";

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Make a request to the /films endpoint to retrieve information about the movie
const filmUrl = `${baseUrl}/films/${movieId}/`;

axios.get(filmUrl)
    .then(response => {
        const filmData = response.data;

        // Retrieve the list of character URLs from the movie data
        const characterUrls = filmData['characters'];

        // Print the characters' names
        Promise.all(characterUrls.map(characterUrl =>
            axios.get(characterUrl)
                .then(characterResponse => console.log(characterResponse.data['name']))
                .catch(error => console.error(`Failed to fetch character data from ${characterUrl}`, error))
        ))
            .catch(error => console.error(error));
    })
    .catch(error => console.error(`Failed to fetch movie data for Movie ID ${movieId}`, error));
