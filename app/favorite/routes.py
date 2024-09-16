from app.models.product import Product
from flask import render_template, session, flash, redirect, url_for
from app.models import storage
from app.models.user import User
from app.models.favorite import Favorite


from app.favorite import bp as favorite_bp


@favorite_bp.route('/favorites')
def favorites():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        favorite_items = storage.all(Favorite).values()
        user_favorites = [item for item in favorite_items if item.user_id == user.id]
        return render_template('favorites.html', favorite_items=user_favorites)
    else:
        flash('You need to log in to access favorites.', 'warning')
        return redirect(url_for('login'))
    
@favorite_bp.route('/add_to_favorites/<string:product_id>', methods=['POST'])
def add_to_favorites(product_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            product = storage.get(Product, product_id)
            if product:
                favorite_item = next((item for item in storage.all(Favorite).values() if item.product_id == product_id and item.user_id == user.id), None)
                
                if favorite_item:
                    flash('Product already in favorites.', 'info')
                else:
                    new_favorite_item = Favorite(user_id=user.id, product_id=product_id)
                    storage.new(new_favorite_item)
                    storage.save()
                    flash('Product added to favorites.', 'success')
            else:
                flash('Product not found.', 'error')
        else:
            flash('User not found. Please log in again.', 'error')
    else:
        flash('You need to log in to add items to favorites.', 'warning')
    
    return redirect(url_for('home.home'))

@favorite_bp.route('/remove_from_favorites/<string:product_id>', methods=['POST'])
def remove_from_favorites(product_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            favorite_item = next((item for item in storage.all(Favorite).values() if item.product_id == product_id and item.user_id == user.id), None)
            if favorite_item:
                storage.delete(favorite_item)
                storage.save()
                flash('Product removed from favorites.', 'success')
            else:
                flash('Product not found in favorites.', 'error')
        else:
            flash('User not found. Please log in again.', 'error')
        return redirect(url_for('favorites'))
    else:
        flash('You need to log in to remove items from favorites.', 'warning')
        return redirect(url_for('login'))

