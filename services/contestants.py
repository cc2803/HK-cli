import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def fetch_contestants(season: int):
    url = f"https://hellskitchen.fandom.com/wiki/Season_{season}#Contestants"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"class": "wikitable"})
    if not table:
        return f"No contestants table found for season {season}.", url

    # Extract headers
    headers = [th.get_text(strip=True) for th in table.find("tr").find_all("th")]

    rows = []
    rowspan_trackers = [None] * len(headers)  # to keep track of rowspans

    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all(["td", "th"])
        row = []

        col_idx = 0
        for i in range(len(headers)):
            # If a rowspan value is carried over, insert it
            if rowspan_trackers[i]:
                row.append(rowspan_trackers[i]["text"])
                rowspan_trackers[i]["rows_left"] -= 1
                if rowspan_trackers[i]["rows_left"] == 0:
                    rowspan_trackers[i] = None
            else:
                if col_idx < len(cells):
                    cell = cells[col_idx]
                    text = cell.get_text(strip=True)
                    row.append(text)

                    # Handle rowspan
                    if cell.has_attr("rowspan"):
                        rowspan_trackers[i] = {
                            "text": text,
                            "rows_left": int(cell["rowspan"]) - 1
                        }
                    col_idx += 1
                else:
                    row.append("")

        # Skip empty rows
        if any(cell.strip() for cell in row):
            rows.append(row)

    return tabulate(rows, headers=headers, tablefmt="grid"), url