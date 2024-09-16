from app.models.product import Product
from flask import render_template, session, redirect, url_for, flash
from app.models import storage
from app.models.user import User
from app.models.cart import Cart
from app.models.cart_item import Cart_item


from app.cart import bp as cart_bp

@cart_bp.route('/cart')
def cart():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            cart_items = storage.all(Cart_item).values()
            user_cart_items = []
            for item in cart_items:
                cart = storage.get(Cart, item.cart_id)
                if cart is not None and cart.user_id == user.id:
                    user_cart_items.append(item)
                elif cart is None:
                    print(f"Warning: Cart with ID {item.cart_id} not found.")
            return render_template('cart.html', cart_items=user_cart_items)
        else:
            flash('User not found. Please log in again.', 'error')
            return redirect(url_for('authentication.login'))
    else:
        flash('You need to log in to access the cart.', 'warning')
        return redirect(url_for('authentication.login'))

# @cart_bp.route('/add_to_cart/<string:product_id>', methods=['POST'])
# def add_to_cart(product_id):
#     if 'user_id' in session:
#         user = storage.get(User, session['user_id'])
#         if user:
#             product = storage.get(Product, product_id)
#             if product:
#                 user_cart = next((cart for cart in storage.all(Cart).values() if cart.user_id == user.id), None)
                
#                 if not user_cart:
#                     user_cart = Cart(user_id=user.id)
#                     storage.new(user_cart)
#                     storage.save()

#                 existing_item = next((item for item in storage.all(Cart_item).values() if item.product_id == product_id and item.cart_id == user_cart.id), None)
                
#                 if existing_item:
#                     flash('Product already in cart.', 'info')
#                 else:
#                     new_cart_item = Cart_item(cart_id=user_cart.id, product_id=product_id)
#                     storage.new(new_cart_item)
#                     storage.save()
#                     flash('Product added to cart.', 'success')
#             else:
#                 flash('Product not found.', 'error')
#         else:
#             flash('User not found. Please log in again.', 'error')
#     else:
#         flash('You need to log in to add items to your cart.', 'warning')
    
#     return redirect(url_for('home.home'))    


from flask import jsonify

@cart_bp.route('/add_to_cart/<string:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            product = storage.get(Product, product_id)
            if product:
                user_cart = next((cart for cart in storage.all(Cart).values() if cart.user_id == user.id), None)
                
                if not user_cart:
                    user_cart = Cart(user_id=user.id)
                    storage.new(user_cart)
                    storage.save()

                existing_item = next((item for item in storage.all(Cart_item).values() if item.product_id == product_id and item.cart_id == user_cart.id), None)
                
                if existing_item:
                    return jsonify({'status': 'error', 'message': 'Product already in cart.'}), 400
                else:
                    new_cart_item = Cart_item(cart_id=user_cart.id, product_id=product_id)
                    storage.new(new_cart_item)
                    storage.save()
                    return jsonify({'status': 'success', 'message': 'Product added to cart.'}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Product not found.'}), 404
        else:
            return jsonify({'status': 'error', 'message': 'User not found. Please log in again.'}), 401
    else:
        return jsonify({'status': 'error', 'message': 'You need to log in to add items to your cart.'}), 403



@cart_bp.route('/remove_from_cart/<string:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            cart_item = next((item for item in storage.all(Cart_item).values() if item.product_id == product_id and storage.get(Cart, item.cart_id).user_id == user.id), None)
            if cart_item:
                storage.delete(cart_item)
                storage.save()
                flash('Product removed from cart.', 'success')
            else:
                flash('Product not found in cart.', 'error')
        else:
            flash('User not found. Please log in again.', 'error')
        return redirect(url_for('carts.cart'))
    else:
        flash('You need to log in to remove items from your cart.', 'warning')
        return redirect(url_for('authentication.login'))