import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

# Write your code below this line 👇

response = requests.get(URL)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')

movie_tags = soup.find_all('div', class_='article-title-description__text')
movie_list = [movie.find(class_='title').getText() for movie in movie_tags]


with open('top-100-movies.txt', 'w') as outfile:
    outfile.writelines(f'{movie}\n' for movie in movie_list[::-1])
