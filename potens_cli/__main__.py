import os
import requests

from PIL import Image
from io import BytesIO

from codebase.search import search_gogo_search,search_gogo_anime_data
from cli.printer import print_choices,print_list,print_ascii
from codebase.stream import stream_web,stream_mpv,stream_vlc

from InquirerPy import inquirer
from rich.console import Console
from rich.text import Text
from ascii_magic import AsciiArt

def main():
    console=Console()

    os.system("clear")

    print_ascii()
    
    query=inquirer.text(message="Search an anime: ").execute()

    res=search_gogo_search(query)
    if res==None:
        console.print(
            Text(
                f"No Results Found"
            ),
            style="bold yellow"
        )
        return
      
    anime_choice=print_choices(res.keys(),"Anime")

    console.print(
        Text(
            f"You've selected {anime_choice}..\nLoading Episodes..."
        ),
        style="bold yellow"
    )

    data=search_gogo_anime_data(res[anime_choice])

    ep_choice=print_list(data["episodes"],"Episode")

    stream_web(anime_choice,ep_choice)
    # stream_vlc(anime_choice,ep_choice)
    # stream_mpv(anime_choice,ep_choice)
    
    

if __name__=="__main__":
    main()
