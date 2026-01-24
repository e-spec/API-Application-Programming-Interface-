import requests

# Base URL for the public PokeAPI (no API key required)
BASE_URL = "https://pokeapi.co/api/v2"

# --------------------------------------------------
# Request basic Pokémon data by name
# --------------------------------------------------
# This sends an HTTP GET request to:
# https://pokeapi.co/api/v2/pokemon/pikachu
response = requests.get(f"{BASE_URL}/pokemon/pikachu", timeout=10)

# Raises an exception if the HTTP response code is 4xx or 5xx
response.raise_for_status()

# Convert the JSON response into a Python dictionary
pokemon = response.json()

# --------------------------------------------------
# Print basic Pokémon attributes
# --------------------------------------------------
print("-----Basic Pokémon Information-----")
print("***P I K A C H U***")
print("Name:", pokemon["name"])
print("ID:", pokemon["id"])
print("Height:", pokemon["height"])
print("Weight:", pokemon["weight"])

# --------------------------------------------------
# Extract and print Pokémon types
# --------------------------------------------------
# "types" is a list of dictionaries
print("\nTypes:")
for t in pokemon["types"]:
    # Each type entry contains a nested "type" object
    print("-", t["type"]["name"])

# --------------------------------------------------
# Extract and print Pokémon abilities
# --------------------------------------------------
print("\nAbilities:")
for a in pokemon["abilities"]:
    # Each ability entry contains an "ability" object
    print("-", a["ability"]["name"])

# --------------------------------------------------
# Retrieve Pokémon species information
# --------------------------------------------------
# The species URL is provided inside the first API response
species_url = pokemon["species"]["url"]

# Send a second GET request to the species endpoint
response = requests.get(species_url, timeout=10)
response.raise_for_status()

# Parse species JSON data
species = response.json()

# Print special classification flags
print("\nIs Legendary:", species["is_legendary"])
print("Is Mythical:", species["is_mythical"])

# --------------------------------------------------
# Retrieve evolution chain data
# --------------------------------------------------
# Evolution data is located at a different endpoint
evolution_url = species["evolution_chain"]["url"]

response = requests.get(evolution_url, timeout=10)
response.raise_for_status()

evolution = response.json()

# --------------------------------------------------
# Print evolution chain
# --------------------------------------------------
print("\nEvolution chain:")

# The evolution structure is hierarchical (nested)
chain = evolution["chain"]

# Base species (first evolution stage)
print("-", chain["species"]["name"])

# First evolution stage(s)
if chain["evolves_to"]:
    for evo in chain["evolves_to"]:
        print("->", evo["species"]["name"])

        # Second evolution stage(s), if present
        if evo["evolves_to"]:
            for evo2 in evo["evolves_to"]:
                print("->", evo2["species"]["name"])
