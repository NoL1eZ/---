# определяем список хабов, которые нам интересны
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers = Headers(os="win", headers=True).generate()
ret = requests.get('https://habr.com/ru/all/', headers=headers)
soup = BeautifulSoup(ret.text, 'html.parser')

articles = soup.find_all('article')
# извлекаем посты
posts = soup.find_all('article', class_='post')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet')
    hubs = [hub.text.lower().split() for hub in hubs]
    for hub in hubs:
        for word in hub:
            if word in KEYWORDS:
                datetime = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                title = article.find(class_='tm-article-snippet__title-link').find('span')
                title = title.text
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                print(f'<{datetime}> - <{title}> - <https://habr.com/ru/all/{href}>')