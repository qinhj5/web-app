# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, render_template, request
from flask_cors import cross_origin
from processors.user import (
    get_user_list,
    is_credential_valid,
    login_user,
    verify_credential,
)

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    return render_template("index.html")


@home_bp.route("/status", methods=["POST"])
@cross_origin()
def status():
    """
    Check user status.
    ---
    tags:
      - Home
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token for user authentication.
      - name: user_info
        in: body
        type: object
        required: true
        description: User information.
        schema:
          type: object
          properties:
            user_id:
              type: string
    responses:
      200:
        description: User status response.
        schema:
          type: object
          properties:
            is_valid:
              type: boolean
    """
    authorization = request.headers.get("Authorization")
    credential = authorization.split(" ")[-1]
    user_info = request.get_json()
    is_valid = False

    if verify_credential(credential, user_info) and is_credential_valid(user_info["user_id"]):
        is_valid = True

    return jsonify({"is_valid": is_valid})


@home_bp.route("/login", methods=["POST"])
@cross_origin()
def login():
    """
    User login.
    ---
    tags:
      - Home
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token for user authentication.
      - name: user_info
        in: body
        type: object
        required: true
        description: User information.
        schema:
          type: object
          properties:
            user_id:
              type: string
    responses:
      200:
        description: Login response.
        schema:
          type: object
          properties:
            is_login:
              type: boolean
    """
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
    """
    Get user list.
    ---
    tags:
      - Home
    responses:
      200:
        description: User list response.
        schema:
          type: object
          properties:
            users:
              type: array
              items:
                type: object
                properties:
                  username:
                    type: string
                  email:
                    type: string
    """
    user_list = get_user_list()
    return jsonify(user_list)
