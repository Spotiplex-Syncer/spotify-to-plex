# app/models/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    spotify_id = db.Column(db.String(120), unique=True, nullable=True)
    plex_id = db.Column(db.String(120), unique=True, nullable=True)
    spotify_token = db.Column(db.String(200), nullable=True)
    plex_token = db.Column(db.String(200), nullable=True)

    # Add any other fields you need for your application
