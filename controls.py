import sqlite3


class UsersControl:
    def __init__(self, db=None):
        self.conn = sqlite3.connect(db, check_same_thread=False) if db else None
        self.cursor = self.conn.cursor()

    def to_arr_dicts(self, data):
        ready_data = []
        for user_tuple in data:
            user = {
                "id": user_tuple[1],
                "name": user_tuple[0]
            }
            ready_data.append(user)
        return ready_data

    def search_users(self, name):
        query = """
        SELECT name, id 
        FROM users
        WHERE name LIKE (?)
        """

        self.cursor.execute(query, (f'%{name}%',))
        users = self.cursor.fetchall()
        return self.to_arr_dicts(users)

    def get_user_data(self, user_id):
        query = """
        SELECT email, age, about
        FROM users_data
        WHERE user_id = (?)"""

        self.cursor.execute(query, (user_id,))
        users_data = self.cursor.fetchone()
        return users_data
