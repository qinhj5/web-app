# -*- coding: utf-8 -*-
from flask import Blueprint
from processors.user import get_user_list

about = Blueprint('about', __name__)


@about.route('/about')
def about_route():
    usernames = get_user_list()
    return f'Thanks for users {", ".join(usernames)}!'
