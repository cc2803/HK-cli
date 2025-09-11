import click
import time

def print_contestant_details(name: str, data: dict):
    """Pretty print contestant details in terminal."""
    url = data["url"]
    intro = data["intro"]

    print(f"Searching for: {name.title()}")
    time.sleep(1.5)
    click.secho("\nIntro:\n",fg="cyan")
    print(intro + "\n")

    click.secho("URL: ",fg="cyan",nl=False)
    click.echo(f"{url}")  