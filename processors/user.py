# -*- coding: utf-8 -*-
import os
import json
import time
import traceback
from google.oauth2 import id_token
from google.auth.transport import requests
from models.user_tab import get_users, get_user_by_user_id, add, update


def get_user_list():
    users = get_users()
    return [{"name": user["name"], "email": user["email"]} for user in users]


def is_credential_valid(user_id):
    user = get_user_by_user_id(user_id)
    if round(time.time() * 1000) > user["expire_time"]:
        return False
    return True


def verify_credential(credential, user_info):
    processors_dir = os.path.abspath(os.path.dirname(__file__))

    client_config_path = os.path.abspath(os.path.join(processors_dir, "../config/client.json"))
    with open(client_config_path) as f:
        client_config = json.load(f)

    client_id = client_config["client_id"]
    try:
        parsed_info = id_token.verify_oauth2_token(credential, requests.Request(), client_id)
    except Exception as e:
        print(f"{e}\n{traceback.format_exc()}")
        return False
    else:
        parsed_user_info = {"user_id": parsed_info.get("sub"),
                            "name": parsed_info.get("name"),
                            "email": parsed_info.get("email"),
                            "credential": credential}

    if parsed_user_info != user_info:
        return False

    return True


def login_user(user_info):
    user = get_user_by_user_id(user_info["user_id"])
    if user:
        update(user_info)
    else:
        add(user_info)
