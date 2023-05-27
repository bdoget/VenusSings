import os
import base64
import json
from dotenv import load_dotenv
import requests

def get_token():
    load_dotenv()
    client_id = os.getenv("SPOTIFY_ID")
    client_secret = os.getenv("SPOTIFY_SECRET")
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def search_tracks(query):
    access_token = get_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    # Set the query parameters for the track search
    params = {
        "q": query,
        "type": "track",
        "limit": 1  # Number of tracks to retrieve
    }
    # Send the request to search for tracks
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    search_results = response.json()["tracks"]["items"][0]["id"]
    return search_results

def main():
    artist = input("Enter artist: ")
    song = input("Enter song: ")
    query = song + " - " + artist
    result = search_tracks(query)
    print(result)

if __name__ == "__main__":
    main()