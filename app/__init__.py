from flask import Flask
from app.logger import init_db

# Create the Flask app
app = Flask(__name__)

init_db()
from app import routes