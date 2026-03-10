import pandas
from constants import print_on_console

class SoundtrackCSV:
  def __init__(self) -> None:
    self._soundtrack_data = {
    "song titles": [],
    "found on spotify": [],
    "spotify URI": [],
  }

  def add_data(self,song_title:str,found_on_spotify:str,uri:str)->None:
    """"""
    self._soundtrack_data["song titles"].append(song_title)
    self._soundtrack_data["found on spotify"].append(found_on_spotify)
    self._soundtrack_data["spotify URI"].append(uri)

  def create_CSV(self,movie_name:str)->None:
    """"""
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