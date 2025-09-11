import click
from services.scrapper import fetch_season_details
from utils.misc import seperator

@click.command(name="season-details")
@click.option("--season", type=int, required=True, help="Season number of Hell's Kitchen")
def cli_command(season):
    """
    Fetch and display details about a Hell's Kitchen season.
    """
    seperator()
    try:
        details = fetch_season_details(season)
        click.secho(f"\nTitle: {details['title']}", fg="cyan", bold=True)
        click.secho("\nIntro: ",fg="cyan",bold=True)
        click.secho(f"{details['intro']}")
        click.secho("\nURL: ",fg="cyan",nl=False) 
        click.secho (f"{details['url']}")
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
    seperator()