# -*- coding: utf-8 -*-
import argparse
from app import app
from models import db
from models.user_tab import init_users


def db_operation(option=None):
    if not option:
        return 
    
    with app.app_context():
        if option == "create":
            db.create_all()
            print("created.")
        elif option == "drop":
            db.drop_all()
            print("dropped.")
        elif option == "recreate":
            db.drop_all()
            db.create_all()
            print("recreated.")
        elif option == "initialize":
            init_users()
            print("initialized.")
        else:
            print(f"option {option} not found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="db operation")
    parser.add_argument("-o", "--option", help="options: create/drop/recreate/initialize", required=True)
    args = parser.parse_args()
    db_operation(option=args.option)
