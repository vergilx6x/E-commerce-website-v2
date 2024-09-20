from flask import Blueprint

# Initialize the blueprint for the products feature
bp = Blueprint('orders', __name__)

from app.order import routes