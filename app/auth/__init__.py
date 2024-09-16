from flask import Blueprint

# Initialize the blueprint for the products feature
bp = Blueprint('authentication', __name__)

from app.auth import routes
