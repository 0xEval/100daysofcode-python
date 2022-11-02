import requests
import dotenv
import os
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from bs4 import BeautifulSoup

dotenv.load_dotenv('.env')
SPOTIFY_CLIENT = os.getenv('SPOTIFY_CLIENT')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

URL = 'https://www.billboard.com/charts/hot-100/2004-01-03/'

response = requests.get(URL)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, 'html.parser')

page_containers = soup.find_all(
    'div', class_='o-chart-results-list-row-container'
)

results = []
for container in page_containers:
    song_title = container.find('h3', id='title-of-a-story')
    song_label = song_title.find_next_sibling()
    results.append(
        {
            'title': song_title.getText().strip(),
            'label': song_label.getText().strip(),
        }
    )


spotify = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT, client_secret=SPOTIFY_SECRET
    )
)

tracklist = []
for track in results:
    result = spotify.search(
        q='track:' + track['title'] + ' artist:' + track['label'],
        type='track',
        limit=1,
    )
    for i in range(len(result['tracks']['items'])):
        try:
            track_uri = result['tracks']['items'][i]['uri']
        except:
            continue
        tracklist.append(track_uri)
        print(track_uri)

scope = 'playlist-modify-private'
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_secret=SPOTIFY_SECRET,
        client_id=SPOTIFY_CLIENT,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=scope,
        show_dialog=True,
        cache_path='token.txt',
    )
)
user_id = spotify.current_user()['id']
playlist = spotify.user_playlist_create(
    user_id,
    '2014-03-1 Billboard 100',
    False,
    False,
    '#100DaysOfCode',
)
spotify.user_playlist_add_tracks(user_id, playlist['id'], tracks=tracklist)
