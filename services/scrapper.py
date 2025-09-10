import requests
from bs4 import BeautifulSoup


def fetch_season_details(season: int) -> dict:
    """
    Fetches details of a given Hell's Kitchen season from fandom.wiki.

    Returns a dictionary with extracted data.
    """
    url = f"https://hellskitchen.fandom.com/wiki/Season_{season}"
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request fails

    soup = BeautifulSoup(response.text, "html.parser")

    # Example: Extract title and first paragraph of the season page
    title = soup.find("h1", {"class": "page-header__title"})
    title_text = title.get_text(strip=True) if title else f"Season {season}"

    # Usually, the intro paragraph is the first <p> in the article content
    intro_paragraph = soup.find("div", {"class": "mw-parser-output"}).find("p")
    intro_text = intro_paragraph.get_text(strip=True) if intro_paragraph else "No description found."

    return {
        "season": season,
        "title": title_text,
        "intro": intro_text,
        "url": url
    }
