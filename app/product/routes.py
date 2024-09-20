from app.models.product import Product
from flask import render_template
from app.models import storage


from app.product import bp as product_bp

@product_bp.route('/product/<string:product_id>')
def product_detail(product_id):
    product = storage.get(Product, product_id)
    return render_template('products.product_detail.html', product=product)