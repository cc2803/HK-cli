import click
from services.scrapper import fetch_season_details


@click.command(name="season-details")
@click.option("--season", type=int, required=True, help="Season number of Hell's Kitchen")
def cli_command(season):
    """
    Fetch and display details about a Hell's Kitchen season.
    """
    try:
        details = fetch_season_details(season)
        click.secho(f"Title: {details['title']}", fg="cyan", bold=True)
        click.echo(f"Intro: {details['intro']}")
        click.echo(f"URL: {details['url']}")
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
