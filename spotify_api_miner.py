
import requests
import json

album = input("Enter album ID: ")
service = "https://dit009-spotify-assignment.vercel.app/api/v1"
url = f"{service}/albums/{album}/tracks"
response = requests.get(url)
data = response.json()

all_songs = data['items']

print(all_songs)