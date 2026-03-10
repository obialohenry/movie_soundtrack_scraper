import pandas
from constants import print_on_console

class SoundtrackCSV:
  """Utility class for generating a CSV file."""
  def __init__(self) -> None:
    self._soundtrack_data = {
    "song titles": [],
    "found on spotify": [],
    "spotify URI": [],
  }

  def add_data(self,song_title:str,found_on_spotify:str,uri:str)->None:
    """ Add soundtrack data for a song to the internal data structure.
    
    Parameters:
      song_title (str): The title of the soundtrack song.
      found_on_spotify (str): Indicates whether the song was found on Spotify.
      uri (str): Spotify track URI if available, otherwise an empty None.
    """
    self._soundtrack_data["song titles"].append(song_title)
    self._soundtrack_data["found on spotify"].append(found_on_spotify)
    self._soundtrack_data["spotify URI"].append(uri)

  def create_CSV(self,movie_name:str)->None:
    """Create a CSV file containing the collected soundtrack data.
    
    Parameter:
      - movie_name (str): Name of movie used in creating a CSV filename.
    
     Behaviors:
        - Converts the stored soundtrack data into a pandas DataFrame.
        - Saves the data as a CSV file.
        - Resets the internal data storage after saving.
    """
    print_on_console("Generating soundtrack CSV file...")
    pandas.DataFrame(self._soundtrack_data).to_csv(f"{movie_name}_soundtracks.csv")
    print_on_console(f"""
    ✅ CSV file saved successfully.
                    
      File saved as : {movie_name}_soundtrack.csv
""", True)
    self._soundtrack_data = {
    "song titles": [],
    "found on spotify": [],
    "spotify URI": [],
    }