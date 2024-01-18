from InquirerPy import inquirer

def print_choices(options,term):
    selected_option=inquirer.rawlist(
        message=f"Pick a {term}: ",
        choices=options,
        default=1,
        multiselect=False,
    ).execute()

    return selected_option