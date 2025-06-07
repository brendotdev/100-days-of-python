import requests
from bs4 import BeautifulSoup

# Ask user for a date in YYYY-MM-DD format
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Billboard URL for that date
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract song titles from the page
song_tags = soup.select("li ul li h3")
songs = [song.get_text(strip=True) for song in song_tags]

# Output the top 100 songs
print(f"\n🎵 Top 100 songs from {date}:\n")
for i, song in enumerate(songs, start=1):
    print(f"{i}. {song}")
