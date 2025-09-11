import click
from services.scrapeName import fetch_contestant_details
from utils.formatting import print_contestant_details
from utils.misc import seperator

@click.command(name="name")
@click.argument("name",nargs=-1)
def cli_command(name):

    """Fetch a quick introduction for contestant/staff with given name."""

    search_name = " ".join(name).strip(" ")
    seperator()
    try:
        if not search_name:
            raise Exception("Please provide a name to search.")

        data = fetch_contestant_details(search_name)
        if not data:
            raise Exception(f"No data found for {search_name}")

        print_contestant_details(search_name, data)
    
    except Exception as e:
        click.secho(f"Error: {e}",fg="red")
    
    seperator()