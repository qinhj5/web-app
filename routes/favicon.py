# -*- coding: utf-8 -*-
from flask import Blueprint, send_from_directory

favicon_bp = Blueprint("favicon", __name__)


@favicon_bp.route("/favicon.ico")
def favicon_route():
    return send_from_directory("static", "favicon.ico", mimetype="image/vnd.microsoft.icon")
