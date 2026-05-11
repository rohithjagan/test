# hello.py (modified)
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchall()
    print("Check")
