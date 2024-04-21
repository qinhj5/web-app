# -*- coding: utf-8 -*-
import json
import os
import time

from flask import current_app
from google.auth.transport import requests
from google.oauth2 import id_token

from models.user_tab import add, get_user_by_user_id, get_users, update


def get_user_list():
    users = get_users()
    return [{"name": user["name"], "email": user["email"]} for user in users]


def is_credential_valid(user_id):
    user = get_user_by_user_id(user_id)
    if not user or round(time.time() * 1000) > user["expire_time"]:
        return False
    return True


def verify_credential(credential, user_info):
    processors_dir = os.path.abspath(os.path.dirname(__file__))

    client_config_path = os.path.abspath(
        os.path.join(processors_dir, "../config/client.json")
    )
    with open(client_config_path) as f:
        client_config = json.load(f)

    client_id = client_config["client_id"]
    try:
        parsed_info = id_token.verify_oauth2_token(
            credential, requests.Request(), client_id
        )
    except Exception as e:
        current_app.logger.warning(f"verify oauth2 token failed, error: {e}")
        return False
    else:
        parsed_user_info = {
            "user_id": parsed_info.get("sub"),
            "name": parsed_info.get("name"),
            "email": parsed_info.get("email"),
            "credential": credential,
        }

    if parsed_user_info != user_info:
        return False

    return True


def login_user(user_info):
    user = get_user_by_user_id(user_info["user_id"])
    if user:
        update(user_info)
        current_app.logger.info(f"""update user info ({user_info["user_id"]}).""")
    else:
        add(user_info)
        current_app.logger.info(f"""add user info ({user_info["user_id"]}).""")
