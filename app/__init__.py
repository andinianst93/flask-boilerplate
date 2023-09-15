from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_session import Session

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)


    db.init_app(app)

    # Route and Custom Error Here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app