from spotify_client import SpotifyClient
import os


# Spotify credentials taken from developer.spotify
SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

spotify = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)


# Find the id of a track with its name and artist name

def getSong(artist, song):
    resp = spotify.search(f"{artist} {song}", search_types="track")
    try:
        id = resp['tracks']['items'][0]['id']
    except IndexError:
        print(f"{artist} and {song} not found!")
        id = None
    return id