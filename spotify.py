
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ID = os.environ["NKEMS_CLIENT_ID"]
SECRET = os.environ["NKEMS_CLIENT_SECRET"]
SCOPE = "playlist-modify-private playlist-modify-public"
REDIRECT_URI = "https://example.com"

class Spotify:
  """"""
  
  def __init__(self):
    self.tracks = []
    self.playlist_id = ""
    self.sp =  spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=ID,
    client_secret=SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
  ))
    
  def search_for_a_song(self,song_title:str)->str:
    """"""
    search_result = self.sp.search(song_title,limit=1,type="track")
    if search_result:
      items = search_result['tracks']['items']
      if items:
        track = items[0]
        return track['uri']
    return ""
  
  def create_a_playlist(self,movie_name:str):
    """"""
    try:
      soundtracks_playlist = self.sp.current_user_playlist_create(
      name=f"{movie_name} Soundtracks",
      public=False
    )
    except spotipy.SpotifyException as e:
      print("Spotify API error:", e)
    else:
      if soundtracks_playlist:
        self.playlist_id = soundtracks_playlist["id"]

  def add_tracks_to_playlist(self)-> None:
    """"""
    self.tracks = []
    result = self.sp.playlist_add_items(self.playlist_id, self.tracks)
    if result:
      print("SUCCESSFULLY ADDED TRACKS TO PLAYLIST")