import requests
import json

def get_lyrics(track_id):
    """
        Returns an array of lyrics
            [dict('startTimeMs': int, 'words': str)] // endtimeMs and syllables don't work
        raises Exception if invalid track_id or no lyrics found or not LINE_SYNCED
    """
    link = f"https://spotify-lyric-api.herokuapp.com/?trackid={track_id}"
    f = requests.get(link)
    
    if f.status_code != 200:
        raise Exception("Error: get_lyrics.py: get_lyrics: status code not 200")
    
    data = json.loads(f.text)
    if data["error"] == True:
        raise Exception("Error: get_lyrics.py: No Lyrics Found")
    if data["syncType"] != "LINE_SYNCED":
        raise Exception("Error: get_lyrics.py: Lyrics are not LINE_SYNCED")
    
    return clean_lyrics(data['lines'])

def clean_lyrics(arr):
    for db in arr:
        del db['endTimeMs']
        del db['syllables']
    return arr


if __name__ == "__main__":
    track_id = "11dFghVXANMlKmJXsNCbNl" # "5f8eCNwTlr0RJopE9vQ6mB"
    lyrics = get_lyrics(track_id)

    print(lyrics)
    print(type(lyrics))
