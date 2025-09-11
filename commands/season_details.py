import click
from services.scrapper import fetch_season_details

terminal_width = 163

@click.command(name="season-details")
@click.option("--season", type=int, required=True, help="Season number of Hell's Kitchen")
def cli_command(season):
    """
    Fetch and display details about a Hell's Kitchen season.
    """
    print("="*terminal_width)
    try:
        details = fetch_season_details(season)
        click.secho(f"Title: {details['title']}", fg="cyan", bold=True)
        click.secho("Intro: ",fg="cyan",bold=True,nl=False)
        click.secho(f"{details['intro']}")
        click.secho("URL: ",fg="cyan",nl=False) 
        click.secho (f"{details['url']}")
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
    print("="*terminal_width)