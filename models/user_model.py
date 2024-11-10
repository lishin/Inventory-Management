# models/user_model.py

import sqlite3
from .database import get_connection
from utils.security import hash_password

class UserModel:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def create_user(self, username, password, role):
        password_hash = hash_password(password)
        try:
            self.cursor.execute('''
                INSERT INTO users (username, password_hash, role)
                VALUES (?, ?, ?)
            ''', (username, password_hash, role))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_user_by_username(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone()

    def update_last_login(self, user_id):
        self.cursor.execute('''
            UPDATE users SET last_login = datetime('now')
            WHERE user_id = ?
        ''', (user_id,))
        self.conn.commit()

    # 其他用户操作...
    # ...

    def close(self):
        self.conn.close()
