from app.models.user import User
from flask import request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import storage


from app.auth import bp as auth_bp



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = storage.get_user(username)
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful.', 'success')
            return redirect(url_for('home.home'))
        else:
            flash('Login failed. Check your username and/or password.', 'error')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        image = request.files.get('image')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        image_url = save_image(image) if image else None
        new_user = User(email=email, password=hashed_password, username=username, image_url=image_url)
        
        try:
            storage.new(new_user)
            storage.save()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('authentication.login'))
        except Exception as e:
            storage.rollback()
            flash(f'Registration failed. Error: {e}', 'error')
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home.home'))

@auth_bp.route('/user_profile')
def user_profile():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('user_profile.html', user=user)
    else:
        flash('You need to log in to access your profile.', 'warning')
        return redirect(url_for('authentication.login'))

@auth_bp.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if request.method == 'POST':
            user.email = request.form.get('email')
            user.username = request.form.get('username')
            user.first_name = request.form.get('first_name')
            user.last_name = request.form.get('last_name')
            image = request.files.get('image')
            if image:
                user.image_url = save_image(image, user.id)
            storage.save()
            flash('Profile updated successfully.', 'success')
            return redirect(url_for('user_profile'))
        return render_template('edit_profile.html', user=user)
    else:
        flash('You need to log in to edit your profile.', 'warning')
        return redirect(url_for('login'))