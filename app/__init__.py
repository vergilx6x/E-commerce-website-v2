from flask import Flask
from app.models import storage

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    from app.routes import bp as home_bp
    from app.auth import bp as auth_bp
    from app.product import bp as product_bp
    from app.cart import bp as cart_bp
    from app.favorite import bp as favorite_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(favorite_bp)

    @app.teardown_appcontext
    def close_db(error):
        storage.close()

    return app
