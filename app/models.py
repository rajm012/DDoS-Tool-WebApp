from flask_login import UserMixin

# Dummy user database (in-memory)
users = {}

# Dummy user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Function to add a new user
def add_user(username, password):
    users[username] = {"password": password}

    