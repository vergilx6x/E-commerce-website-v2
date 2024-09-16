from flask import Blueprint

# Initialize the blueprint for the products feature
bp = Blueprint('favorites', __name__)

from app.favorite import routes