# К слову, эта хераборина парсит mangalib, но пока не очень эффективно
# timely unused

from bs4 import BeautifulSoup
from selenium import webdriver

def getpage(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    driver.get(url)
    html = driver.page_source
    return html


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
page = getpage("https://mangalib.me/kawai-dake-janai-onnanoko/")
soup = BeautifulSoup(page, "html.parser") # супчег
# Poster
poster_url = soup.find("div", class_="media-sidebar__cover paper").img['src']

# Title
main_title = soup.find('div', class_='media-name__main').text
# Chapters
# chapters = soup.find_all('div', class_='vue-recycle-scroller__item-wrapper')
# Page Url
# url_parsed = soup.find("meta", property="og:site_name")
# Description
description = soup.find(itemprop="description").get("content")

# categories
genres_unfil = soup.find("a", class_='media-tag-item ')
genres = [p.contents[0] for p in genres_unfil]

print(f"title: {main_title}, \nposter: {poster_url}, \ndescription: {description}, \ngenres: {genres}")