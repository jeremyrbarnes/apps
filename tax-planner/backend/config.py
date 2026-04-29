import os
from dotenv import load_dotenv

# Load the .env file once
load_dotenv()

class Config:
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-123')
    
    # Logic to ensure the correct 2026 driver is used
    _db_url = os.environ.get('DATABASE_URL', '')
    if _db_url.startswith("postgresql://"):
        _db_url = _db_url.replace("postgresql://", "postgresql+psycopg://", 1)
    
    SQLALCHEMY_DATABASE_URI = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    # In prod, we might want stricter security settings