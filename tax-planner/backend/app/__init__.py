from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

# The function must be named exactly create_app
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)   
    
    # Load your config
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://...' 
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app import models

    # Register blueprints or models here
    return app