from codebase.search import search_gogo_search,search_gogo_episodes
from cli.printer import print_choices,print_list
from codebase.stream import stream_web

from InquirerPy import inquirer
from rich.console import Console
from rich.text import Text

def main():
    console=Console()
    
    query=inquirer.text(message="Search an anime: ").execute()

    res=search_gogo_search(query)
    anime_choice=print_choices(res.keys(),"Anime")

    console.print(
        Text(
            f"You've selected {anime_choice}..\nLoading Episodes..."
        ),
        style="bold yellow"
    )

    ep_list=search_gogo_episodes(res[anime_choice])

    ep_choice=print_list(ep_list,"Episode")

    stream_web(anime_choice,ep_choice)
    
    

if __name__=="__main__":
    main()
