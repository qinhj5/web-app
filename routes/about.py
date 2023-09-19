# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from processors.user import get_user_list

about = Blueprint('about', __name__)


@about.route('/about')
def about_route():
    usernames = get_user_list()
    message = f'Supported by {", ".join(usernames)}.'
    return render_template('about.html', message=message)
