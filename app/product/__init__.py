from flask import Blueprint

# Initialize the blueprint for the products feature
bp = Blueprint('products', __name__)

from app.product import routes