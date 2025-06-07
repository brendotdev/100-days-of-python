import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Step 1: Get Billboard Top 100 from a given date
date = input("What date do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(billboard_url)
soup = BeautifulSoup(response.text, "html.parser")
song_titles = [song.getText(strip=True) for song in soup.select("li ul li h3")]

# Step 2: Authenticate with Spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",  # Must match your Spotify Developer settings
        client_id="YOUR_SPOTIFY_CLIENT_ID",
        client_secret="YOUR_SPOTIFY_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Step 3: Search for each song on Spotify
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found on Spotify. Skipped.")

# Step 4: Create a new playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Step 5: Add songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Playlist '{playlist['name']}' created with {len(song_uris)} songs.")
