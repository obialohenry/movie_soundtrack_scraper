import pandas

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
    pandas.DataFrame(self._soundtrack_data).to_csv(f"{movie_name}_soundtracks.csv")
    self._soundtrack_data = {
    "song titles": [],
    "found on spotify": [],
    "spotify URI": [],
    }