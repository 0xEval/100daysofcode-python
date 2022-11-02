from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

articles = soup.find_all('span', class_='titleline')
sublines = soup.find_all('span', class_='subline')

result = []
for article, subline in zip(articles, sublines):
    article_tag = article.find('a')
    score_tag = subline.find('span', class_='score')
    article_text = article_tag.getText()
    article_link = article_tag.get('href')
    score_text = int(score_tag.getText().split()[0])
    result.append(
        {
            'title': article_text,
            'link': article_link,
            'votes': score_text,
        },
    )

sorted_result = sorted(result, key=lambda d: d['votes'], reverse=True)
pprint(sorted_result)
