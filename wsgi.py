"""
WSGI entry point for production deployment
Run with: gunicorn wsgi:app
"""
from backend.app import create_app
from backend.config import Config

app = create_app(Config)

