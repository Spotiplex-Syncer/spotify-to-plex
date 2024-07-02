from authlib.integrations.flask_client import OAuth

# Spotify OAuth Config
SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
SPOTIFY_REDIRECT_URI = "http://localhost:5000/auth/spotify/callback"

# Plex OAuth Config
PLEX_CLIENT_ID = "your_plex_client_id"
PLEX_CLIENT_SECRET = "your_plex_client_secret"
PLEX_REDIRECT_URI = "http://localhost:5000/auth/plex/callback"


# instance/config.py

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:C4jbz8c6CfGvdLWh5M8t4fpUR0WVeYbKNBmrAP9Pdt3NrGVVprNe9UxOZGl5goJ8@192.168.1.209:5432/postgres"
SQLALCHEMY_TRACK_MODIFICATIONS = False  # To avoid overhead
