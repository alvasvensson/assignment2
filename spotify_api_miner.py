import requests
import json

def import_related_artists_api(artist_id):
    service = "https://dit009-spotify-assignment.vercel.app/api/v1"
    url = f"{service}/artists/{artist_id}/related-artists"
    response = requests.get(url)
    data = response.json()

    return data

def save_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def main():
    artist_id = input("Find related artists.\n Please enter an ID of an artist:  ")

    result = import_related_artists_api(artist_id)
    print(result)

if __name__ == "__main__":
    main()