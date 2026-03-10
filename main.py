from movies_soundtrack import MoviesSoundtrack
from spotify import Spotify
from wikipedia_movie_page import WikipediaMoviePage
from soundtrack_csv import SoundtrackCSV
from constants import print_on_console


print(
      """
    🎬 Movie Soundtrack Scraper

    This tool extracts soundtrack songs from a movie's Wikipedia page
    and creates a Spotify playlist with those songs.
      """
    )

is_running = True

wikipedia_movie_page = WikipediaMoviePage()
movies_soundtrack = MoviesSoundtrack()
spotify = Spotify()
soundtrack_csv = SoundtrackCSV()
def users_choice()-> int:
    """"""
    while True:
      try:
        choice = int(input("Enter choice: "))
      except ValueError:
        print_on_console("Please enter only numbers (1 or 2).")
        continue
      
      if choice == 1:
          return 1
      elif choice == 2:
          return 2
      else:
         print_on_console("Select only numbers 1 or 2.")
           
def run():
  while is_running:
    # ---------- PROMPT THE USER TO ENTER A MOVIE NAME ---------- #

    movie_name = input("Enter the movie name you want to scrape the soundtrack for: ").title()
    if movie_name:
      movie_soundtrack_page_url = wikipedia_movie_page.get_page(movie_name)  
    else:
       print("Movie name cannot be empty. Please try again.")
       continue

    # ---------- LOCATE AND SCRAPE THE MOVIES SOUNDTRACK PAGE ON WIKIPEDIA ---------- #
    if movie_soundtrack_page_url:
      movie_page_html = movies_soundtrack.get_movie_page_html(movie_soundtrack_page_url)
      soundtrack_section = movies_soundtrack.get_soundtrack_tag(movie_page_html)
      tracks = movies_soundtrack.get_all_track_tags(soundtrack_section)
    else:
       continue

    # ---------- EXTRACT ALL SOUNDTRACK SONG TITLES ---------- #
    if movies_soundtrack.get_soundtrack_titles(tracks):
      pass
    else:
      continue
    
    # ---------- SEARCH FOR EACH SONG USING THE SPOTIFY WEB API ---------- #
    print_on_console("Searching for songs on Spotify...")
    for song_title in movies_soundtrack.soundtrack:
      song = spotify.search_for_a_song(song_title)
      if song:
          soundtrack_csv.add_data(song_title=song_title,found_on_spotify="Yes",uri=song)
          spotify.tracks.append(song)
      else:
          soundtrack_csv.add_data(song_title=song_title,found_on_spotify="No",uri="None")
    print()

    # ---------- CREATE A NEW PRIVATE SPOTIFY PLAYLIST ---------- #
    
    spotify.create_a_playlist(movie_name)

    # ---------- ADD ALL SUCCESSFULLY FOUND TRACKS TO THE PLAYLIST ---------- #

    spotify.add_tracks_to_playlist()

    # ---------- GENERATE A CSV FILE CONTAINING THE SCRAPED SONG TITLES ---------- #

    soundtrack_csv.create_CSV(movie_name)

    print_on_console("""
  🎉 Done!

  Your soundtrack playlist and CSV file have been created successfully.
  """, True)
    
    print_on_console("""
  Would you like to scrape another movie soundtrack?

  1. Yes
  2. Exit
  """, True)
   
    result = users_choice()

    if result == 1:
       continue
    elif result == 2:
       print_on_console("👋 Thank you for using the Movie Soundtrack Scraper!")
       break

 
if __name__ == "__main__":
   run()