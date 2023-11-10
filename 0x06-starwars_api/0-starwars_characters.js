#!/usr/bin/node
import sys
import request


if len(sys.arv) < 2:
    print("Usage: Python 0-starwars_characters.js <Movie ID")
    sys.exit(1)

# define the Star_war API base url
base_url = "https://swapi.dev/api"

# Get the movie id fromthe command-line arguments
movie_id = sys.argv[1]

# Make a request to the /films endpoint to retrieve information
film_url = f"[base_url}/films/{movie_id}/"
response = requests.get(film_url)

# Check if request was successful
if response.status_code == 200:
    film_data = response.json()
    
    # Retrieve the list of character URLs from the movie data
    characters_urls = 'characters'

    # Print the characters' names
    for character_url in character_urls:
        character_response = requests.get(character_url)
        if character_response.status_code == 200:
            character_data = character_response.json()
            print(character_data['name'])
        else:
            print(f"Failed to fetch character data from {character_url}")
else:
    print(f"Failed to fetch movie data for Movie ID {movie_id}")
