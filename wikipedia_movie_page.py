import requests
from constants import WIKIPEDIA_HEADER

WIKIPEDIA_URL = "https://en.wikipedia.org/w/api.php"
SOUNDTRACK = "soundtrack"

class WikipediaMoviePage:
  """"""
  
  def __init__(self) -> None:
    pass

  def get_url(self,movie_name:str) -> str:
    """"""
    params = {
        "action":"query",
        "list":"search",
        "srsearch": f"{movie_name} {SOUNDTRACK}",
        "utf8":"",
        "format": "json"
    }
    try:
      response = requests.get(url=WIKIPEDIA_URL,headers=WIKIPEDIA_HEADER,params=params)
      response.raise_for_status()
    except Exception as e:
       print("API error", e)
       return ""
    else:
      response_json = response.json()
      movie_titles = response_json["query"]["search"]
      movie_title = self._search_for_a_movie_title(movie_titles,SOUNDTRACK).replace(" ","_")
      if  movie_title:
        return f"https://en.wikipedia.org/wiki/{movie_title}"
      else:
        print(f"Could not get {movie_name} Wikipedia's Soundtrack page.")
      return ""

  def _search_for_a_movie_title(self,movies:list[dict],value)-> str:
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
  