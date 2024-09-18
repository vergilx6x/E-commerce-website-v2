from flask import Blueprint

# Initialize the blueprint for the products feature
bp = Blueprint('home', __name__)

from app.home import routes