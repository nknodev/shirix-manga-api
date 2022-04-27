# ReadManga Scraper
import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}

def rm_info(url):
  page = requests.get(url, headers=headers)
  if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser") # супчег
    title = soup.find('span', class_="name").text
    shiki = requests.get(f"https://shikimori.one/api/mangas?search={title}", headers=headers).json()
    shiki_s = shiki[0]
    shiki_id = shiki_s['id']
    shiki_material = requests.get(f"https://shikimori.one/api/mangas/{shiki_id}", headers=headers).json()
    pics = shiki_s['image']
    description = soup.find(itemprop="description").get("content")
    rating_rm = soup.find(itemprop="ratingValue").get("content")
    vols_unfil = soup.find('div', class_="subject-meta").p.text.replace("\n", "")
    vols = vols_unfil.split(":")[1].split(",")[0].replace(" ", "")
    chapters = soup.select(".mt-3 a")[0].contents[0].split("-")[1].replace(" ", "")
    last_chapter_link_rm = soup.find("a", class_="chapter-link read-last-chapter").href
    pub = soup.find("span", class_="elem_publisher").text.replace(" ", "")
    genres_unfil = soup.find_all("a", class_="element-link")
    pic_original = f"https://shikimori.one{pics['original']}"
    pic_preview = f"https://shikimori.one{pics['preview']}"
    pic_x96 = f"https://shikimori.one{pics['x96']}"
    pic_x48 = f"https://shikimori.one{pics['x48']}"
    pics_shiki = {
"original": pic_original,
"preview": pic_preview,
"x96": pic_x96,
"x48": pic_x48
}
    genres_unfil_1 = [p.get_text() for p in genres_unfil]
    genres = list(set(genres_unfil_1))
    
    return {"success": True, "message": "ohhh yeah", "result": [{"title" : title, "description": description, "shikimori_id": int(shiki_id), "pictures": pics_shiki, "publisher": pub,  "vols": int(vols), "chapters": int(chapters), "rm_rating": rating_rm, "rm_url": url, "genres": genres}]}, 200
  else:
    return {"success": False, "message" : "Context Searching Error"}, 402




def rm_search(q, only_manga=False):
  if only_manga:
    req = requests.get(url, headers=headers)
  else:
    results = requests.get(f'https://readmanga.io/search/suggestion?query={q}', headers=headers).json()['suggestions'] # results
    result = results[0]
    return f"https://readmanga.io{result['link']}"
