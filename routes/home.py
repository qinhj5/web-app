# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, jsonify
from processors.user import verify_credential, is_credential_valid, login_user, get_user_list

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    return render_template("index.html")


@home_bp.route("/status", methods=["POST"])
def status():
    authorization = request.headers.get("Authorization")
    credential = authorization.split(" ")[-1]
    user_info = request.get_json()
    is_valid = False

    if verify_credential(credential, user_info) and is_credential_valid(user_info["user_id"]):
        is_valid = True

    return jsonify({"is_valid": is_valid})


@home_bp.route("/login", methods=["POST"])
def login():
    authorization = request.headers.get("Authorization")
    credential = authorization.split(" ")[-1]
    user_info = request.get_json()
    is_login = False

    if verify_credential(credential, user_info):
        login_user(user_info)
        is_login = True

    return jsonify({"is_login": is_login})


@home_bp.route("/users", methods=["GET"])
def users():
    user_list = get_user_list()
    return jsonify(user_list)
