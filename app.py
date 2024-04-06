# -*- coding: utf-8 -*-
import os
import json
from models import db
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger


def create_app():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    flask_app = Flask(__name__)

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

    flask_app.config["CORS_HEADERS"] = "Authorization"
    CORS(flask_app)

    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config["title"] = "web-app API"
    swagger_config["version"] = "1.0"
    swagger_config["description"] = "[Tutorial](https://blog.csdn.net/embracestar/article/details/132919569)"
    swagger_config["termsOfService"] = "https://github.com/qinhjs/web-app"
    swagger_config["specs"] = [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ]
    Swagger(flask_app, config=swagger_config)

    return flask_app


app = create_app()
