from entities.user import User
import sqlite3

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        cursor = self._connection.cursor()
        
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user
    
    def find_user(self, username, password):
 
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
            
        if user:
            return User(user["username"], user["password"]) 
        else:
            return None
