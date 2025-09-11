import click
from services.contestants import fetch_contestants
from utils.misc import seperator

@click.command(name="contestants")
@click.option("--season", required=True, type=int, help="Season number")
def cli_command(season):
    """Fetch and display contestants of a season."""

    seperator()
    try:
        table, url = fetch_contestants(season)
        print(f"Contestants of Season {season}:\n")
        print(table)
        print(f"\nURL: {url}")
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
    
    seperator()