
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from constants import print_on_console

# Load environment variables from .env file
load_dotenv()

ID = os.environ["CLIENT_ID"]
SECRET = os.environ["CLIENT_SECRET"]
SCOPE = "playlist-modify-private playlist-modify-public"
REDIRECT_URI = "https://example.com"

class Spotify:
  """"""
  
  def __init__(self):
    print_on_console("Connecting to Spotify...")
    self.tracks = []
    self.playlist_id = ""
    self.sp =  spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=ID,
    client_secret=SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
  ))
    print_on_console("✅ Successfully authenticated with Spotify.", True)
    
  def search_for_a_song(self,song_title:str)->str:
    """"""
    search_result = self.sp.search(song_title,limit=1,type="track")
    if search_result:
      items = search_result['tracks']['items']
      if items:
        track = items[0]
        print_on_console(f"✅ Found: {song_title}",)
        return track['uri']
    print_on_console(f"❌ Not found on Spotify: {song_title}",)
    return ""
  
  def create_a_playlist(self,movie_name:str)-> None:
    """"""
    print_on_console("Creating Spotify playlist for this movie...")
    try:
      soundtracks_playlist = self.sp.current_user_playlist_create(
      name=f"{movie_name} Soundtracks",
      public=False
    )
    except spotipy.SpotifyException as e:
      print("Spotify API error:", e)
    else:
      if soundtracks_playlist:
        print_on_console("✅ Playlist successfully created.", True)
        self.playlist_id = soundtracks_playlist["id"]

  def add_tracks_to_playlist(self)-> None:
    """"""
    print_on_console("Adding songs to the playlist...")
    result = self.sp.playlist_add_items(self.playlist_id, self.tracks)
    if result:
      print_on_console(f"✅ {len(self.tracks)} songs added to the playlist.", True)
      self.tracks = []