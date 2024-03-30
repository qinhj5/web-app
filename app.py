# -*- coding: utf-8 -*-
import os
import json
from models import db
from flask import Flask
from flask_cors import CORS


def create_app():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    flask_app = Flask(__name__)
    CORS(flask_app)
    flask_app.config["CORS_HEADERS"] = "Authorization"

    mysql_config_path = os.path.abspath(os.path.join(root_dir, "config/mysql.json"))
    with open(mysql_config_path) as f:
        mysql_config = json.load(f)

    mysql_user = mysql_config.get("user")
    mysql_password = mysql_config.get("password")
    mysql_host = mysql_config.get("host")
    mysql_database = mysql_config.get("database")
    mysql_uri = f"""mysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}"""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri

    secret_config_path = os.path.abspath(os.path.join(root_dir, "config/secret.json"))
    with open(secret_config_path) as f:
        secret_config = json.load(f)

    flask_app.config["SECRET_KEY"] = secret_config.get("key")

    from routes.home import home_bp
    flask_app.register_blueprint(home_bp)

    db.init_app(flask_app)

    return flask_app


app = create_app()
