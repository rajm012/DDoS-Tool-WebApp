from flask_login import UserMixin
from app.database import get_user

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def get(user_id):
        user_data = get_user(user_id)  # Fetch user data by user_id
        if user_data:
            return User(user_data['id'], user_data['username'])
        return None