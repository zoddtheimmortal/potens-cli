import requests

from bs4 import BeautifulSoup
from config.urls import URLS

def search_gogo_search(query):
    base=URLS["site_urls"]["gogoanime"]
    url=f"{base}/search.html"
    response=requests.get(url,params={"keyword":query})

    soup=BeautifulSoup(response.content,"html.parser")

    animes={}
    for row in soup.select("ul.items li"):
        title=row.find('p',class_="name").find('a').get_text()
        link=row.find('p',class_="name").find('a').get("href")
        animes[title]=f"{base}{link}"
    
    return animes

def search_gogo_episodes(query):
    return "kid named finger"