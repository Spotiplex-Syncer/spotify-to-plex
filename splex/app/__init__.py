from flask import Flask
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth
from .models.models import (
    db,
)  # Adjust the import path for your User model and database setup
from .services.confighandler import read_config  # Adjust if necessary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_filename="../instance/config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Setup Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = "auth.show_login"
    login_manager.init_app(app)

    # OAuth Setup with Direct Config Access
    oauth = OAuth(app)
    oauth.register(
        name="spotify",
        client_id=app.config["SPOTIFY_CLIENT_ID"],
        client_secret=app.config["SPOTIFY_CLIENT_SECRET"],
        access_token_url="https://accounts.spotify.com/api/token",
        authorize_url="https://accounts.spotify.com/authorize",
        api_base_url="https://api.spotify.com/v1",
        client_kwargs={
            "scope": "user-read-private playlist-modify-public playlist-modify-private"
        },
        redirect_uri=app.config["SPOTIFY_REDIRECT_URI"],
    )

    # Ensure OAuth and other services are initialized after Flask-Login and DB
    from .routes.auth_routes import auth_bp

    app.register_blueprint(auth_bp)

    return app
