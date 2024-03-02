from InquirerPy import inquirer
from rich.console import Console
from rich.text import Text

def print_choices(options,term):
    selected_option=inquirer.select(
        message=f"Pick a {term}: ",
        choices=options,
        default=1,
        multiselect=False,
    ).execute()

    return selected_option

def print_list(options,term):
    console=Console()
    for option in options:
        console.print(
            Text(
                f"{option}",
                style="green"
            )
        )

    selected_option=inquirer.text(message=f"Select A(n) {term}: ").execute()

    return selected_option

def print_ascii():
    console=Console()
    console.print(
            Text(r"""
                 __                             ___ 
    ____  ____  / /____  ____  _____      _____/ (_)
   / __ \/ __ \/ __/ _ \/ __ \/ ___/_____/ ___/ / / 
  / /_/ / /_/ / /_/  __/ / / (__  )_____/ /__/ / /  
 / .___/\____/\__/\___/_/ /_/____/      \___/_/_/   
/_/                                                 
"""), style="bold magenta"
    )
    return