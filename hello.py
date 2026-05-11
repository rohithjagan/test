import sqlite3

def delete_user(username):
    conn = sqlite3.connect("users.db")
    query = f"DELETE FROM users WHERE username = '{username}'"
    conn.execute(query)
    conn.commit()
