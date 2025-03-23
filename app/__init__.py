from flask import Flask, abort, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Create the Flask app
app = Flask(__name__)
app.secret_key="supersecretkey123"

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if unauthorized

# Dummy user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Dummy user database
users = {"admin": {"password": "password"}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Initialize Flask-Limiter
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