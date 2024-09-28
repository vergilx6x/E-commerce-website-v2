from flask import Blueprint, render_template, redirect, url_for, flash, request
from markupsafe import escape
from app.models import storage
from app.models.product import Product
from app.models.category import Category


from app.home import bp as home_bp


@home_bp.route('/home', strict_slashes=False)
@home_bp.route('/', strict_slashes=False)
def home():
    categories = storage.all(Category).values()
    all_products = list(storage.all(Product).values())
    all_products.sort(key=lambda p: p.created_at, reverse=True)
    new_products = all_products[:10]

    return render_template('home.html', categories=categories, new_products=new_products, all_products=all_products)

@home_bp.route('/home/category/<string:category_id>')
def category(category_id):
    category = storage.get(Category, category_id)
    if category:
        products = [product for product in storage.all(Product).values() if product.category_id == category_id]
        return render_template('category.html', category=category, products=products)
    else:
        flash('Category not found.', 'error')
        return redirect(url_for('home.home'))