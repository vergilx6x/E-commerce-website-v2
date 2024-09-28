import os
from flask import url_for, request, flash, redirect, render_template
from werkzeug.utils import secure_filename
from config import Config
from app.models import storage
from app.models.category import Category
from app.models.product import Product

from app.utils import bp as utils_bp 


def save_image(file, identifier=None):
    if file and Config.allowed_file(file.filename):
        # Sanitize the identifier to ensure it's a valid filename
        sanitized_name = secure_filename(identifier) if identifier else secure_filename(file.filename)
        # Extract the file extension from the uploaded file
        file_extension = os.path.splitext(file.filename)[1].lower()
        # Construct the filename with the proper extension
        filename = f"{sanitized_name}{file_extension}"
        file_path = os.path.join(Config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # Return the URL to access the image
        return url_for('static', filename='uploads/' + filename)
    return None

@utils_bp.route('/search', methods=['GET'])
def search():
    # query = request.args.get('query')
    query = request.args.get('query', '')
    if not query:
        flash('Please enter a search query.', 'warning')
        return redirect(url_for('home.home'))
    
    
    page = request.args.get('page', 1, type=int)
    products = [p for p in storage.all(Product).values() if query.lower() in p.name.lower()]
    
    # Pagination settings
    per_page = 6
    total_products = len(products)
    paginated_products = products[(page - 1) * per_page:page * per_page]


    # Search for products
    # products = [p for p in storage.all(Product).values() if query.lower() in p.name.lower()]

    # Search for categories
    categories = [c for c in storage.all(Category).values() if query.lower() in c.name.lower()]

    return render_template('search_results.html', query=query, products=paginated_products, total_products=total_products, page=page, per_page=per_page, categories=categories)