# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, send_from_directory

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    return render_template("home.html")


@home_bp.route("/favicon.ico")
def favicon_route():
    return send_from_directory("static", "favicon.ico", mimetype="image/vnd.microsoft.icon")
