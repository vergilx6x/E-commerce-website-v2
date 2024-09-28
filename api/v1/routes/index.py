#!/usr/bin/python3
""" Index """
from app.models.cart import Cart
from app.models.cart_item import Cart_item
from app.models.category import Category
from app.models.favorite import Favorite
from app.models.order import Order
from app.models.order_item import Order_item
from app.models.product import Product
from app.models import storage
from api.v1.routes import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Cart, Cart_item, Category, Favorite, Order, Order_item, Product]
    names = ["Cart", "Cart_item", "Category", "Favorite", "Order", "Order_item", "Product"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)