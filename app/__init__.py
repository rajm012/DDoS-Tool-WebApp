from flask import Flask, abort, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from app.database import init_db, close_db, get_user
from app.models import User


# Create the Flask app
app = Flask(__name__)
app.secret_key="supersecretkey123"


init_db()
app.teardown_appcontext(close_db)


# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    user_data = get_user(user_id)
    if user_data:
        return User(user_data['id'], user_data['username'])

    return None

# limiter to limit the access as for subscription 
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# List of blocked IPs
BLOCKED_IPS = ["192.168.1.100"]  # Add IPs to block

# Middleware to block IPs
@app.before_request
def block_ips():
    if request.remote_addr in BLOCKED_IPS:
        abort(403)  # Forbidden

# Import routes after creating the app to avoid circular imports
from app import routes