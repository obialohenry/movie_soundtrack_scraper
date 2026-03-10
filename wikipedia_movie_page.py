import requests
from constants import WIKIPEDIA_HEADER,print_on_console

WIKIPEDIA_URL = "https://en.wikipedia.org/w/api.php"
SOUNDTRACK = "soundtrack"

class WikipediaMoviePage:
    """Utility class that searches Wikipedia for the movies's soundtrack page."""
    
    def __init__(self) -> None:
      pass

    def get_page(self,movie_name:str) -> str:
      """Get a movie Wikipedia Page URL
      
      Parameter:
        - movie_name: The movie whose soundtrack page is being searched for.
      
      Behaviors:
        - Searches Wikipedia for the movie's soundtrack page using the Wikipedia API and retrieves the correct page URL.

      Returns:
        str: The movie soundtrack page URL if found, otherwise an empty string.
      """
      params = {
          "action":"query",
          "list":"search",
          "srsearch": f"{movie_name} {SOUNDTRACK}",
          "utf8":"",
          "format": "json"
      }
      try:
        print_on_console("🌐 Searching for the movie page on Wikipedia...")
        response = requests.get(url=WIKIPEDIA_URL,headers=WIKIPEDIA_HEADER,params=params)
        response.raise_for_status()
      except Exception:
        print_on_console("""
          ❌ An error occured.
          Please check the your internet and try again.
            """, True
          )
        return ""
      else:
        response_json = response.json()
        movie_titles = response_json["query"]["search"]
        movie_title = self._search_for_a_movie_title(movie_titles,SOUNDTRACK).replace(" ","_")
        if  movie_title:
          print_on_console("✅ Movie page found.", True)
          return f"https://en.wikipedia.org/wiki/{movie_title}"
        else:
          print_on_console("""
            ❌ Could not find a Wikipedia page for this movie.
            Please check the spelling and try again.
            """, True
          )
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
  