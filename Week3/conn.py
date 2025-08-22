import sqlite3

DB_NAME = "YBCOLLEGE.db"

def get_connection():
    """Return a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)
