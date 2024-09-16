from flask import Blueprint

# Initialize the blueprint for the products feature
bp = Blueprint('carts', __name__)

from app.cart import routes