import click
import time
from tabulate import tabulate

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

def print_bookmarks(rows, page, per_page, total):
    """Pretty print bookmarks in table format."""
    if not rows:
        print(f"No bookmarks found on page {page}.")
        return

    headers = ["ID", "URL", "Description", "Timestamp"]
    print("\n" + tabulate(rows, headers=headers, tablefmt="grid"))
    print(f"\nPage {page} of {(total // per_page) + (1 if total % per_page else 0)} | Total bookmarks: {total}")

def print_bookmark_row(row):
    """
    Pretty print a single bookmark row (tuple) in table format.
    """
    if not row:
        print("No bookmark found.")
        return

    # Ensure row is wrapped in a list, because tabulate expects a list of rows
    if isinstance(row, tuple):
        row = [row]

    headers = ["ID", "URL", "Description", "Timestamp"]
    print("\n" + tabulate(row, headers=headers, tablefmt="grid"))