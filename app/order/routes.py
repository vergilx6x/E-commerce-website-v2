
from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.models import storage
from app.models.user import User
from app.models.order import Order

from app.order import bp as order_bp

@order_bp.route('/user/<string:user_id>/orders')
def user_orders(user_id):
    if 'user_id' in session:
        user = storage.get(User, user_id)
        if user:
            orders = [order for order in storage.all(Order).values() if order.user_id == user_id]
            return render_template('user_orders.html', orders=orders, user=user)
        else:
            flash('User not found.', 'error')
            return redirect(url_for('home.home'))
    else:
        flash('You need to log in to view orders.', 'warning')
        return redirect(url_for('authentication.login'))
    
@order_bp.route('/orders', methods=['POST'])
def add_order():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            data = request.get_json()
            status = data.get('status', 'pending')
            total_amount = data.get('total_amount', 0)

            new_order = Order(user_id=user.id, status=status, total_amount=total_amount)
            storage.new(new_order)
            storage.save()

            return redirect(url_for('orders.user_orders'))
        else:
            flash('User not found. Please log in again.', 'error')
            return redirect(url_for('authentication.login'))
    else:
        flash('You need to log in to add an order.', 'warning')
        return redirect(url_for('authentication.login'))
    
@order_bp.route('/orders/<string:order_id>', methods=['POST'])
def delete_order(order_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            order = storage.get(Order, order_id)
            if order and order.user_id == user.id:
                storage.delete(order)
                storage.save()
                flash('Order deleted successfully.', 'success')
                # Redirect to user orders with user_id
                return redirect(url_for('orders.user_orders', user_id=user.id))
            else:
                flash('Order not found or you are not authorized to delete this order.', 'error')
                return redirect(url_for('orders.user_orders', user_id=user.id))
        else:
            flash('User not found. Please log in again.', 'error')
            return redirect(url_for('authentication.login'))
    else:
        flash('You need to log in to delete an order.', 'warning')
        return redirect(url_for('authentication.login'))