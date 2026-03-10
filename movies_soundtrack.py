import requests
from bs4 import BeautifulSoup
from constants import WIKIPEDIA_HEADER, print_on_console

class MoviesSoundtrack:
   """"""

   def __init__(self) -> None:
      self.soundtrack = []
   
   def get_movie_page_html(self,page_url:str)-> str:
      """"""
      try:
        movie_page_response = requests.get(page_url,headers=WIKIPEDIA_HEADER)
        movie_page_response.raise_for_status()
      except Exception as e:
         print("API error", e)
         return ""
      else:
        return  movie_page_response.text
    
   def get_soundtrack_tag(self,movie_page:str):
    """"""
    soup = BeautifulSoup(movie_page,'html.parser')
    return  soup.find("table", class_="tracklist")
   
   def get_all_track_tags(self,soundtrack_tag):
     """"""
     print_on_console("Looking for the soundtrack section on the page...")
     if soundtrack_tag:
      print_on_console("✅ Soundtrack section located.")
      return soundtrack_tag.find_all("tr")[1:-1]
     else:
       print_on_console("❌ No soundtrack section found for this movie.", True)
       return []
     
   def _get_a_tracks_cell(self,track_tag):
     return track_tag.td
   
   def get_soundtrack_titles(self,tracks_tag)-> bool:
    """"""
    self.soundtrack = []
    print_on_console("Extracting soundtrack titles...")
    if tracks_tag:
      for track_tag in tracks_tag:
         cell = self._get_a_tracks_cell(track_tag)

         if cell:
            title = cell.get_text(strip=True)
            song_title = ''
            if '"' in title:
               song_title = title.split('"')[1]
               self.soundtrack.append(song_title)
            else:
              self.soundtrack.append(title)
         else:
           return False
    else:
      return False
    print_on_console(message=f"Found {len(self.soundtrack)} songs in the soundtrack.", space_after_message=True)
    return True
      