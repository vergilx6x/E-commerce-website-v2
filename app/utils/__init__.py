from flask import Blueprint

# Initialize the blueprint for the products feature
bp = Blueprint('utils', __name__)

from app.utils import routes