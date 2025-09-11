import requests
from bs4 import BeautifulSoup
from utils.misc import formatContent

def build_contestant_url(name: str) -> str:
    """
    Convert a contestant name into a valid Wiki URL.
    e.g. "jessica vogel" -> "https://hellskitchen.fandom.com/wiki/Jessica_Vogel"
    """
    wiki_name = name.title().replace(" ", "_")
    return f"https://hellskitchen.fandom.com/wiki/{wiki_name}"


def fetch_contestant_details(name: str):
    """Fetch contestant intro and stats from the Hell's Kitchen wiki page."""
    url = build_contestant_url(name)
    response = requests.get(url)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Intro/description
    description = soup.find("meta", property="og:description")
    intro = description["content"] if description else "No description found."
    intro = formatContent(intro)

    return {
        "url": url,
        "intro": intro
    }
