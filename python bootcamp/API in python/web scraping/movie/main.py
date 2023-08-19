import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200611015421/https://www.empireonline.com/movies/features/best-tv-shows-ever-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.find_all(name='h3', class_='title')

movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]

with open('movie.txt', mode='w') as file:
    for Movie in movies:
        file.write(f'{Movie}\n')
