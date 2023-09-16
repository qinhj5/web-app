# -*- coding: utf-8 -*-
import argparse
from app import app
from models import db
from models.user_tab import init_users


def db_operation(func=None):
    with app.app_context():
        if func == "create":
            db.create_all()
            print("created.")
        elif func == "drop":
            db.drop_all()
            print("dropped.")
        elif func == "recreate":
            db.drop_all()
            db.create_all()
            print("recreated.")
        elif func == "init_users":
            init_users()
            print("initialized.")
        else:
            print(f"{func} not found.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='db operation')
    parser.add_argument('-f', '--func', help='function: create/drop/recreate/init_users', required=True)
    args = parser.parse_args()
    db_operation(func=args.func)
