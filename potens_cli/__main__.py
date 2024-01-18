from codebase.search import search_gogo
from cli.printer import print_choices
from InquirerPy import inquirer
from rich.console import Console
from rich.text import Text

def main():
    console=Console()
    
    query=inquirer.text(message="Search an anime: ").execute()

    res=search_gogo(query)
    choice=print_choices(res.keys(),"Anime")

    console.print(
        Text(
            f"You've selected {choice}..\nLoading Episodes..."
        ),
        style="bold yellow"
    )

    
    

if __name__=="__main__":
    main()
