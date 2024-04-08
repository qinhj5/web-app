# -*- coding: utf-8 -*-
import os
import json
from models import db
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_wtf.csrf import CSRFProtect


def init_db(flask_app):

    mysql_config_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "config/mysql.json"))
    with open(mysql_config_path) as f:
        mysql_config = json.load(f)

    mysql_user = mysql_config.get("user")
    mysql_password = mysql_config.get("password")
    mysql_host = mysql_config.get("host")
    mysql_database = mysql_config.get("database")
    mysql_uri = f"""mysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}"""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri

    db.init_app(flask_app)

    return flask_app


def init_secret(flask_app):

    secret_config_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "config/secret.json"))
    with open(secret_config_path) as f:
        secret_config = json.load(f)

    flask_app.config["SECRET_KEY"] = secret_config.get("key")

    CSRFProtect(flask_app)

    return flask_app


def init_cors(flask_app):

    flask_app.config["CORS_HEADERS"] = "Authorization"

    CORS(flask_app)

    return flask_app


def init_swagger(flask_app):

    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config["title"] = "WEB APP API"
    swagger_config["version"] = "1.0"
    swagger_config["description"] = "[Tutorial](https://blog.csdn.net/embracestar/article/details/132919569)"
    swagger_config["termsOfService"] = "https://github.com/qinhj5/web-app"
    swagger_config["specs"] = [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True
        }
    ]
    Swagger(flask_app, config=swagger_config)

    return flask_app


def create_app(flask_app):

    from routes.home import home_bp
    flask_app.register_blueprint(home_bp)

    flask_app = init_swagger(init_cors(init_secret(init_db(flask_app))))

    return flask_app


app = create_app(Flask(__name__))
