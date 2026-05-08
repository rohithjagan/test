# hello.py (modified)
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE id = {user_id}"   # SQL injection
    return conn.execute(query).fetchall()
