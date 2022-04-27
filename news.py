# News Scraper
import requests
from bs4 import BeautifulSoup


def lastpost():
  url = 'https://shikimori.one'
  # читать дальше слабонервным воспрещено
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
  page = requests.get(url, headers=headers)
  if page.status_code == 200:
    # парсим
    filteredNews = [] # отсеянные новости
    allNews = [] # все новости страницы
    soup = BeautifulSoup(page.text, "html.parser") # супчег
    allNews = soup.findAll('article', class_='b-news_wall-topic')
    lastArticle = allNews[0]
    posterClass = soup.find_all('div', class_='poster')[0]
    # дикпик

    
    for a in posterClass.find_all('img'):
      lastpic = a['src']
    
    lastPost = soup.findAll('div', class_='title')[0]
    lptext = lastPost.text # текст поста
    lastpostlink = lastPost['href'] # ссыла на последний пост
    return {"title" : lptext,"link": lastpostlink, "description_html": '',"poster": lastpic, 'statusApi': 200}, 200
  else:
    return {"error" : "Scrapping error", 'statusApi': 200}, page.status_code
