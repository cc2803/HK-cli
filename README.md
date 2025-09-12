
# HK-cli

**HK-cli** is a command-line interface (CLI) tool that provides trivia and statistics from the reality TV show *Hell's Kitchen*. Developed in Python, this tool offers various commands to fetch contestants, season trivia, and manage bookmarks related to the show.

---

## Features

* **Contestants**: Retrieve a list of contestants from a specific season.
* **Season Details**: Fetch season-specific information.
* **Bookmarks**: Save and manage URLs with descriptions and timestamps.
* **Name**: Get a quick introduction and stats for a contestant or staff member.

---

## Installation

### Prerequisites

Ensure you have Python 3.7+ installed. You can check your Python version with:

```bash
python --version
```

### Clone the Repository

```bash
git clone https://github.com/cc2803/HK-cli.git
cd HK-cli
```

### Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### General Help

```bash
python app.py --help
```

Output:

```
Usage: app.py [OPTIONS] COMMAND [ARGS]...

  Hell's Kitchen Trivia CLI.

Options:
  --help  Show this message and exit.

Commands:
  bookmark        Add a new bookmark with optional description.
  bookmarks       View bookmarks with pagination.
  contestants     Fetch and display contestants of a season.
  name            Fetch a quick introduction for contestant/staff with stats.
  season-details  Fetch and display details about a Hell's Kitchen season.
```

---

### Commands

#### `contestants`

Fetch and display contestants of a specific season.

```bash
python app.py contestants --season <season_number>
```

#### `season-details`

Fetch detailed information about a season.

```bash
python app.py season-details --season <season_number>
```

#### `name`

Fetch a quick introduction for a contestant or staff member.

```bash
python app.py name "<full_name>"
```

#### `bookmark`

Add a new bookmark with an optional description.

```bash
python app.py bookmark <url>
```

#### `bookmarks`

View bookmarks with pagination (10 per page).

```bash
python app.py bookmarks -view -page <page_number>
```

---


## License

This project is licensed under the GNU General Public License v3.0.

---

You're welcome to open a pull request or submit an issue with any constructive suggestions to help improve this project.
