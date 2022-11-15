KEYWORDS = ['дизайн', 'фото', 'web', 'python']

import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers = Headers(os="win", headers=True).generate()
ret = requests.get('https://habr.com/ru/all/', headers=headers)
soup = BeautifulSoup(ret.text, 'html.parser')

articles = soup.find_all('article')
# print(articles)
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet')
    hubs = [hub.text.lower() for hub in hubs]
    for hub in hubs:
        if hub in KEYWORDS or hub.replace(' *', '') in KEYWORDS:
            print(hub)


