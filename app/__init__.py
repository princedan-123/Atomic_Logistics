"""A module that sets up the flask app."""
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from routes import admin_blueprint, views_blueprint
import os

def initialize_app():
    """Initializing the app."""
    load_dotenv()
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('jwt')
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # Testing phase
    app.register_blueprint(views_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    jwt = JWTManager(app)
    return app