import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

ID = os.environ["NKEMS_CLIENT_ID"]
SECRET = os.environ["NKEMS_CLIENT_SECRET"]
SCOPE = "playlist-modify-private playlist-modify-public"
REDIRECT_URI = "https://example.com"

# Spotify client with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=ID,
    client_secret=SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    username="Mitchelle"
))

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

is_running = True

def search_for_a_movie_title(movies:list[dict],value)-> str:
  """Search for a movie title containing a given text.
  
  Parameters:
    - movies (list[dict]): A list of movies and their title's
    - value (str): A substring contained in the movie titles.

  Returns:
    str: The first movie title that contains the value, or an empty string if no match is found.
  """
  value = value.lower()
  for movie in movies:
    if value in movie["title"].lower():
      return movie["title"]
  return ""

while is_running:

  # ---------- PROMPT THE USER TO ENTER A MOVIE NAME ---------- #

  movie_name = input("Enter a movie name: ").title()
  WIKIPEDIA_URL = "https://en.wikipedia.org/w/api.php"
  SOUNDTRACK = "soundtrack"
  WIKEPEDIA_PARAMS = {
    "action":"query",
    "list":"search",
    "srsearch": f"{movie_name} {SOUNDTRACK}",
    "utf8":"",
    "format": "json"
  }
  headers = {
    "User-Agent": "MovieSoundtrackScraper/1.0 (obilaorchisomebi123@gmail.com)"
  }
  WIKIPEDIA_MOVIE_PAGE_URL = ""

  response = requests.get(url=WIKIPEDIA_URL,headers=headers,params=WIKEPEDIA_PARAMS)
  response.raise_for_status()
  response_json = response.json()
  movie_titles = response_json["query"]["search"]
  movie_title = search_for_a_movie_title(movie_titles,SOUNDTRACK).replace(" ","_")
  if  movie_title:
    print(f"Movie Title: {movie_title}")
    WIKIPEDIA_MOVIE_PAGE_URL = f"https://en.wikipedia.org/wiki/{movie_title}"
    print(f"Wikipedia Movie Page: { WIKIPEDIA_MOVIE_PAGE_URL}")
  else:
    print(f"Could not get {movie_name} Wikipedia's Soundtrack page.")
    break
  
  # ---------- LOCATE AND SCRAPE THE MOVIES SOUNDTRACK PAGE ON WIKIPEDIA ---------- #
  soundtrack_song_titles = []
  print()
  movie_page_response = requests.get(WIKIPEDIA_MOVIE_PAGE_URL,headers=headers)
  movie_page_response.raise_for_status()
  movie_page = movie_page_response.text

  soup = BeautifulSoup(movie_page,'html.parser')
  track_list_tag = soup.find("table", class_="tracklist")

  # ---------- EXTRACT ALL SOUNDTRACK SONG TITLES ---------- #
  if track_list_tag:
      soundtrack_title_rows = track_list_tag.find_all("tr")[1:-1]

      for title_row in soundtrack_title_rows:
         cell = title_row.td

         if cell:
            title = cell.get_text(strip=True)
            print(title)
            song_title = ''
            if '"' in title:
               song_title = title.split('"')[1]
            soundtrack_song_titles.append(song_title)
      print(soundtrack_song_titles)
  else:
      print("Tracklist table not found!")
      break
  
  # ---------- SEARCH FOR EACH SONG USING THE SPOTIFY WEB API ---------- #
  user_id = ""
  track_uris = []
  
  current_user = sp.current_user()
  if current_user:
    user_id = current_user['id']
    print(user_id)

  def search_for_a_song(song_title:str)->str:
    """"""
    search_result = sp.search(song_title,limit=1,type="track")
    if search_result:
      items = search_result['tracks']['items']
      if items:
        track = items[0]
        print(f"Spoitify URI for {song_title}: {track['uri']}")
        return track['uri']
    return ""

  for song_title in soundtrack_song_titles:
     song = search_for_a_song(song_title)
     if song:
        track_uris.append(song)

  # ---------- CREATE A NEW PRIVATE SPOTIFY PLAYLIST ---------- #

  try:
    soundtracks_playlist = sp.user_playlist_create(user=user_id, name=f"{movie_name} Soundtracks", public=False)
    print(soundtracks_playlist)
  except spotipy.SpotifyException as e:
     print("Spotify API error:", e)



  #  playlist_add_items(playlist_id, items, position=None)

  #   Adds tracks/episodes to a playlist

  #   Parameters:

  #           playlist_id - the id of the playlist

  #           items - a list of track/episode URIs or URLs

  #           position - the position to add the tracks