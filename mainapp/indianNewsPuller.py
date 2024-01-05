import requests

API_KEY = "7a0191969c1145c3849ac4c6e5fab665"

main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=7a0191969c1145c3849ac4c6e5fab665'
news = requests.get(main_url).json()
 # print(news)
article = news['articles']

news_title = []
for title in article:
    news_title.append(title['title'])

for all_titles in range(len(news_title)):
    a = f'{news_title[all_titles]}'

news_author = []
for authors in article:
    news_author.append(authors['author'])

for all_authors in range(len(news_author)):
    b = f'{news_author[all_authors]}'

news_desc = []
for desc in article:
    news_desc.append(desc['description'])

for all_desc in range(len(news_desc)):
    c = f'{news_desc[all_desc]}'

news_link = []
for link in article:
    news_link.append(link['url'])

for all_links in range(1):
    d = f'{news_link[all_links]}'

for i in range(0, 20):
    main = f'{i+1} | TITLE: {news_title[i]} | AUTHOR: {news_author[i]} | DESCRIPTION: {news_desc[i]} | URL: {news_link[i]}'
    print(main)