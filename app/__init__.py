from flask import Flask, abort, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Create the Flask app
app = Flask(__name__)

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