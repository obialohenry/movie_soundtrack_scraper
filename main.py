# ---------- Project Summary ---------- #
# 1. Prompt the user to enter a movie name
# 2. Locate and scrape the movie's soundtrack page on Wikipedia.
# 3. Extract all soundtrack song titles.
# 4. Search for each song using the Spotify web API.
# 5. Create a new private Spotify Playlist.
# 6. Add all successfully found track to the playlist.
# 7. Generate a CSV file containing the scraped song titles.
# The CSV should represent:
# - The scraped title
# - Whether it was found on spotify, and the spotify URI.

# Spotify Web API Docs: "https://developer.spotify.com/documentation/web-api?utm_source=chatgpt.com"
# This is where you'll find endpoints for:
# Searching tracks, Creating playlists, Adding tracks to playlist, Authentication with OAuth.

# Example Wikipedia Soundtrack Pages
# Black Panther: Wakanda Forever: "https://en.wikipedia.org/wiki/Black_Panther%3A_Wakanda_Forever_%28soundtrack%29?utm_source=chatgpt.com"
# Barbie the Album: "https://en.wikipedia.org/wiki/Barbie_the_Album?utm_source=chatgpt.com"