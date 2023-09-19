# -*- coding: utf-8 -*-
import json
import os
from flask import Flask
from models import db


def get_config(config_path=None):
    with open(config_path) as f:
        config = json.load(f)
        return config


def create_app():
    current_directory = os.getcwd()
    config_path = os.path.join(current_directory, "config.json")
    conf = get_config(config_path=config_path)

    flask_app = Flask(__name__)
    flask_app.config["SECRET_KEY"] = conf.get("SECRET_KEY")
    db_conf = conf.get("SQLALCHEMY_DATABASE")
    db_uri = f"""mysql://{db_conf.get("user")}:{db_conf.get("pwd")}@{db_conf.get("ip")}/{db_conf.get("db")}"""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

    from routes.home import home
    flask_app.register_blueprint(home)

    from routes.about import about
    flask_app.register_blueprint(about)

    db.init_app(flask_app)

    return flask_app


app = create_app()
