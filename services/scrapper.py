import requests
from bs4 import BeautifulSoup
import textwrap
from utils.misc import formatContent

def fetch_season_details(season: int) -> dict:
    """
    Fetches details of a given Hell's Kitchen season from fandom.wiki.

    Returns a dictionary with extracted data.
    """
    url = f"https://hellskitchen.fandom.com/wiki/Season_{season}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract metadata
    title = soup.find("meta", property="og:title")
    description = soup.find("meta", property="og:description")
    page_url = soup.find("meta", property="og:url")
    intro_text = description["content"] if description else "No description found."
    intro_text = formatContent(intro_text)
    intro_text = textwrap.fill(intro_text, width=150)

    return {
        "season": season,
        "title": title["content"] if title else f"Season {season}",
        "intro": intro_text,
        "url": page_url["content"] if page_url else url
    }

