import sqlite3
from config import DATABASE_PATH

def initialize_database():
    """Initializes the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def store_knowledge(key, value):
    """Stores knowledge in the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO knowledge (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def retrieve_knowledge(key):
    """Retrieves knowledge from the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM knowledge WHERE key=?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Initialize the database when this module is imported
initialize_database()