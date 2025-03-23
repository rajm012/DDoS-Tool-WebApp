import sqlite3
from flask import g

DATABASE = 'config/users.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def add_user(username, password):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    return True

def get_user(identifier):
    conn = get_db()
    cursor = conn.cursor()

    if isinstance(identifier, int) or (isinstance(identifier, str) and identifier.isdigit()):  # Fetch by user_id
        user_id = int(identifier)  # Convert to integer
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))

    else:  # Fetch by username
        cursor.execute('SELECT * FROM users WHERE username = ?', (identifier,))
    user_data = cursor.fetchone()

    return user_data
