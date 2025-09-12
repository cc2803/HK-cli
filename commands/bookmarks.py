import click
from services.bookmark_service import get_bookmarks, count_bookmarks
from utils.formatting import print_bookmarks
from utils.misc import seperator

@click.command(name="bookmarks")
@click.option("-view", is_flag=True, help="View saved bookmarks.")
@click.option("-page", default=1, type=int, help="Page number to view (10 per page).")
def cli_command(view, page):
    """View bookmarks with pagination."""
    seperator()
    try:
        if not view:
            click.secho("Use -view option to display bookmarks.", fg="yellow")
            seperator()
            return

        total = count_bookmarks()
        rows = get_bookmarks(page, per_page=10)
        print_bookmarks(rows, page, 10, total)
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
    seperator()
