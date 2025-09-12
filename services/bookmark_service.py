import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "bookmarks.db"

def init_db():
    """Initialize database and table if not exists."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            description TEXT,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_bookmark(url: str, description: str = "") -> dict:
    """
    Add a bookmark to the DB.
    Returns:
        - {'status': 'added', 'row': row_data} if new bookmark was added
        - {'status': 'exists', 'row': row_data} if duplicate exists
    """
    init_db()  # ensure table exists
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if URL already exists
    cursor.execute("SELECT id, url, description, timestamp FROM bookmarks WHERE url = ?", (url,))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        return {'status': 'exists', 'row': existing}

    # Insert new bookmark
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO bookmarks (url, description, timestamp) VALUES (?, ?, ?)",
        (url, description, timestamp)
    )
    conn.commit()
    bookmark_id = cursor.lastrowid
    conn.close()

    return {'status': 'added', 'row': (bookmark_id, url, description, timestamp)}


def get_bookmarks(page: int = 1, per_page: int = 10):
    """Fetch bookmarks for a given page."""
    init_db()
    offset = (page - 1) * per_page
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, url, description, timestamp FROM bookmarks ORDER BY id ASC LIMIT ? OFFSET ?",
        (per_page, offset)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def count_bookmarks():
    """Return total number of bookmarks."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bookmarks")
    total = cursor.fetchone()[0]
    conn.close()
    return total
