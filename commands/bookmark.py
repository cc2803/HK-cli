import click
from services.bookmark_service import add_bookmark
from utils.misc import seperator
from utils.formatting import print_bookmark_row

@click.command(name="bookmark")
@click.argument("url")
def cli_command(url):
    """Add a new bookmark with optional description."""
    seperator()
    try:
        description = click.prompt("Enter a description", default="")
        result = add_bookmark(url, description)
        if result['status']=="added":
            click.secho(f"Bookmark added: {url}", fg="green")
        else:
            click.secho(f"Bookmark with URL: {url} already exists",fg="yellow")
            print_bookmark_row(result['row'])
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
    seperator()
