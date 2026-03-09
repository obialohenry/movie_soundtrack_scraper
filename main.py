from movies_soundtrack import MoviesSoundtrack
from spotify import Spotify
from wikipedia_movie_page import WikipediaMoviePage
from soundtrack_csv import SoundtrackCSV

is_running = True

wikipedia_movie_page = WikipediaMoviePage()
movies_soundtrack = MoviesSoundtrack()
spotify = Spotify()
soundtrack_csv = SoundtrackCSV()

while is_running:

  # ---------- PROMPT THE USER TO ENTER A MOVIE NAME ---------- #

  movie_name = input("Enter a movie name: ").title()
  movie_soundtrack_page_url = wikipedia_movie_page.get_url(movie_name)  

  # ---------- LOCATE AND SCRAPE THE MOVIES SOUNDTRACK PAGE ON WIKIPEDIA ---------- #
  soundtrack_song_titles = []
  print()
  movie_page = movies_soundtrack.get_movie_page(movie_soundtrack_page_url)
  soundtrack_tag = movies_soundtrack.get_soundtrack_tag(movie_page)
  tracks_tag = movies_soundtrack.get_all_track_tags(soundtrack_tag)

  # ---------- EXTRACT ALL SOUNDTRACK SONG TITLES ---------- #
  if movies_soundtrack.get_soundtrack_titles(tracks_tag):
    print(movies_soundtrack.soundtrack)
  else:
    break
  
  # ---------- SEARCH FOR EACH SONG USING THE SPOTIFY WEB API ---------- #
  
  for song_title in movies_soundtrack.soundtrack:
     song = spotify.search_for_a_song(song_title)
     if song:
        soundtrack_csv.add_data(song_title=song_title,found_on_spotify="Yes",uri=song)
        spotify.tracks.append(song)
     else:
        soundtrack_csv.add_data(song_title=song_title,found_on_spotify="No",uri="None")

  # ---------- CREATE A NEW PRIVATE SPOTIFY PLAYLIST ---------- #
  
  spotify.create_a_playlist(movie_name)

  # ---------- ADD ALL SUCCESSFULLY FOUND TRACKS TO THE PLAYLIST ---------- #

  spotify.add_tracks_to_playlist()

  # ---------- GENERATE A CSV FILE CONTAINING THE SCRAPED SONG TITLES ---------- #

  soundtrack_csv.create_CSV(movie_name)