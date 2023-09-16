# -*- coding: utf-8 -*-
from models.user_tab import get_users


def get_user_list():
    users = get_users()
    usernames = [user["username"] for user in users]
    return usernames
