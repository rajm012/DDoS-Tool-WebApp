from flask import Flask
from app.logger import init_db

# Create the Flask app
app = Flask(__name__)

init_db()
from app import routes

# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

# # Initialize Flask-Limiter
# limiter = Limiter(
#     app=app,
#     key_func=get_remote_address,
#     default_limits=["200 per day", "50 per hour"]
# )