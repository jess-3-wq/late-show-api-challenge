from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, JWT_SECRET_KEY
from server.controllers import auth_controller, guest_controller, episode_controller, appearance_controller

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    
    from server.models import user, guest, episode, appearance

    
    from .controllers import auth_controller, guest_controller, episode_controller, appearance_controller

    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(guest_controller.bp)
    app.register_blueprint(episode_controller.bp)
    app.register_blueprint(appearance_controller.bp)

    return app
