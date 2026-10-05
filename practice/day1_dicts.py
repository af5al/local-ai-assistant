import json

"""
Store movies in a Python list.
Save the list to a JSON file.
Load the movies back from the JSON file.
Calculate the average rating.
Handle a missing JSON file without crashing.
"""

movies = [
    {"title": "Inception", "rating": 8.8},
    {"title": "Interstellar", "rating": 8.7},
    {"title": "The Dark Knight", "rating": 9.0}
]

with open('moviesList.json', 'w') as f:
    json.dump(movies, f, indent=4)

with open('moviesList.json', 'r') as f:
    print(f.read())


for movie in movies:
  if(movie["rating"] > 8): print(movie)



