# -*- coding: utf-8 -*-
from models.user_tab import get_users


def get_user_list():
    users = get_users()
    return [{"name": user["name"], "email": user["email"]} for user in users]
