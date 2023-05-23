from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
url = 'https://www.billboard.com/charts/hot-100/'
response = requests.get(url + date)

web_html = response.text
soup = BeautifulSoup(web_html, 'html.parser')
song_titles = soup.find_all(name='h3',
                            class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
song_title = [songs.get_text().strip() for songs in song_titles]
print(song_title)

clint_id = "212cdfac361d463e837c86234ddcbdc1"
clint_screat = "b64dd9d424eb43db8f0940ec0dc947ba"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-private',
                                               redirect_uri="http://example.com",
                                               client_id=clint_id,
                                               client_secret=clint_screat,
                                               cache_path='token.txt',
                                               show_dialog=True
                                               )

                                                )
user_id = sp.current_user()["id"]
