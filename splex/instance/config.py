from authlib.integrations.flask_client import OAuth
from ..services.confighandler import read_config  # Import the read_config function

# Spotify OAuth Config
SPOTIFY_CLIENT_ID = 'your_spotify_client_id'
SPOTIFY_CLIENT_SECRET = 'your_spotify_client_secret'
SPOTIFY_REDIRECT_URI = 'http://localhost:5000/auth/spotify/callback'

# Plex OAuth Config
PLEX_CLIENT_ID = 'your_plex_client_id'
PLEX_CLIENT_SECRET = 'your_plex_client_secret'
PLEX_REDIRECT_URI = 'http://localhost:5000/auth/plex/callback'
