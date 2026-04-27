from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app) # Allows your React frontend to talk to this API

    # --- Models ---
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password_hash = db.Column(db.String(128)) # Use werkzeug.security to hash this!

    # --- Routes ---
    @app.route('/login', methods=['POST'])
    def login():
        # In a real app, verify the password_hash here
        username = request.json.get('username')
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    @app.route('/api/tax-data', methods=['GET'])
    @jwt_required()
    def get_data():
        current_user = get_jwt_identity()
        return jsonify(message=f"Hello {current_user}, here is your tax data.")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)