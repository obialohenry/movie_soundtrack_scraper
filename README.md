# movie_soundtrack_scraper

A command-line Python project that scrapes movie soundtrack titles from Wikipedia and automatically creates a Spotify playlist containing those songs.

The tool retrieves soundtrack songs from a movie's Wikipedia page, searches for them on Spotify using the Spotify Web API, and generates a playlist along with a CSV report of the results.

This project performs tasks such as:

  - Searching for a movie soundtrack page on Wikipedia.
  - Extracting soundtrack song titles
  - Searching songs on Spotify
  - Creating a private Spotify playlist
  - Adding found tracks to the playlist
  - Generating a CSV report of all scraped songs and their Spotify  status

## Features

### Wikipedia Movie Page Search
Searches Wikipedia for the movie's soundtrack page using the Wikipedia API and retrieves the correct page URL.

### Soundtrack Extraction
Scrapes the soundtrack section from the movie page and extracts all song titles listed in the tracklist table.

### Spotify Song Search
Searches each soundtrack song on Spotify and retrieves the corresponding Spotify URI if available.

### Automatic Playlist Creation
Creates a new private Spotify playlist named after the movie soundtrack.

### Add Songs to Playlist
Adds all successfully found songs to the created Spotify playlist.

### CSV Report Generation
Generates a CSV file containing:
  - Song title
  - Whether the song was found on Spotify
  - Spotify track URI (if available)

### Command-Line Interface (CLI)
  - Interactive CLI prompts the user to enter a movie name
  - Displays progress messages while tasks are running
  - Handles invalid input gracefully
  - Allows users to scrape multiple movie soundtracks in a single session
  - Provides clear feedback for errors (missing soundtrack page, network issues, etc.)

## Tech Stack
  - Python 3
  - Requests (HTTP requests)
  - BeautifulSoup (HTML parsing)
  - Spotipy (Spotify API wrapper)
  - Pandas (CSV generation)
  - Object-Oriented Programming (Class-based modular design)

## How to Run
### 1.Install Dependencies
pip install requests beautifulsoup4 pandas spotipy python-dotenv

### 2.Create a Spotify Developer App
Create an application on the Spotify Developer Dashboard and obtain:
  - Client ID
  - Client Secret
Add them to a `.env` file:
  - CLIENT_ID=your_client_id
  - CLIENT_SECRET=your_client_secret

### 3.Run the Program
python main.py

## How it Works
  - The program prompts the user to enter a movie name.
  - It searches Wikipedia for the movie's soundtrack page using the Wikipedia API.
  - The page HTML is parsed using BeautifulSoup to locate the soundtrack tracklist table.
  - Song titles are extracted from the table rows.
  - Each song is searched on Spotify using the Spotify Web API.
  - A new private playlist is created on Spotify.
  - All successfully found tracks are added to the playlist.
  - A CSV file is generated summarizing the results.

The application is structured using modular classes:
  - `WikipediaMoviePage` - Handles Wikipedia API saerch for soundtrack pages
  - `MoviesSoundtrack` - Scrapes soundtrack titles from the page
  - `Spotify` - Handles Spotify authentication, search, playlist creation, and track insertion
  - `SoundtrackCSV` - Generates CSV reports of scraped songs

The CLI guides the user through the process and allows multiple movies to be processed without restarting the program.

## Author
Henry Obialor
