import requests

from bs4 import BeautifulSoup
from config.urls import URLS
from rich.console import Console
from rich.text import Text


HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

def search_gogo_search(query):
    base=URLS["site_urls"]["gogoanime"]
    url=f"{base}/search.html"
    response=requests.get(url,params={"keyword":query},headers=HEADERS)

    soup=BeautifulSoup(response.content,"html.parser")

    animes={}
    for row in soup.select("ul.items li"):
        title=row.find('p',class_="name").find('a').get_text()
        link=row.find('p',class_="name").find('a').get("href")
        animes[title]=f"{base}{link}"
    if len(animes)==0:
        return None
    return animes

def search_gogo_anime_data(link):
    url=f"{link}"

    response=requests.get(url,headers=HEADERS)

    soup=BeautifulSoup(response.content,"html.parser")
    
    data={}

    body=soup.find("div",class_="anime_info_body_bg")
    title=body.find("h1").get_text()
    img=body.find("img").get("src")

    episodes=[]
    for ep in soup.select("ul#episode_page li"):
        ep_start=ep.find('a').get("ep_start")
        ep_end=ep.find('a').get("ep_end")
        episodes.append(f"{ep_start} - {ep_end}")

    data["episodes"]=episodes
    data["title"]=title
    data["img"]=img

    return data

def search_gogo_vid(anime,ep):
    base=URLS["site_urls"]["gogoanime"]
    query=anime.lower().replace(" ","-")
    url=f"{base}/{query}-episode-{ep}"
    console=Console()

    response=requests.get(url,headers=HEADERS)
    
    soup=BeautifulSoup(response.content,"html.parser")
    
    title=soup.find('div',class_="anime_video_body").find('h1').get_text()
    play=soup.find('div',class_="anime_video_body").find('iframe').get("src")
    
    console.print(
        Text(
            f"Now playing {title}...",
            style="yellow bold"
        )
    )

    return play