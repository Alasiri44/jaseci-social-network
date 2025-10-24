from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models.__init_ import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    
    # Initializing extensions
    migrate.init_app(app, db)
    db.init_app(app)
    
    # Importing models
    from models import (user, user_interest, post, notification, message, like, interest, follow, comment, connection )   

    return app