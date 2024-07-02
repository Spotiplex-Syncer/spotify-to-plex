from flask import (
    Blueprint,
    redirect,
    url_for,
    session,
    request,
    jsonify,
    render_template,
)
from flask_login import login_user, logout_user, current_user
from authlib.integrations.flask_client import OAuth

# from ..services.config_handler import read_config  # Adjust the import path as needed
from ..models.models import User  # Adjust the import path for your User model
from flask import current_app

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
oauth = OAuth()

# Assuming oauth.init_app(app) is called in your app factory


@auth_bp.route("/login")
def show_login():
    return render_template("login.html")


@auth_bp.route("/login/spotify")
def login_spotify():
    spotify = oauth.create_client("spotify")
    redirect_uri = url_for("auth.authorize_spotify", _external=True)
    return spotify.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/spotify")
def authorize_spotify():
    spotify = oauth.create_client("spotify")
    token = spotify.authorize_access_token()
    resp = spotify.get("me")
    profile = resp.json()
    user = User.query.filter_by(spotify_id=profile["id"]).first()
    if not user:
        user = User(spotify_id=profile["id"], name=profile["display_name"])
        # Add user saving logic here
    login_user(user, remember=True)
    return redirect("/dashboard")  # Redirect to a dashboard or home page
