# -*- coding: utf-8 -*-
import traceback
from models import db


class UserTab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User(id={self.id}, username={self.username})>'

    def to_dict(self):
        model_dict = dict()
        for c in self.__table__.columns:
            value = getattr(self, c.name, None)
            if value is None:
                value = ''
            model_dict[c.name] = value
        return model_dict


def add_into_database(user_info):
    try:
        email = user_info['email']
        record = UserTab.query.filter(UserTab.email == email).first()
        if record:
            UserTab.query.filter(UserTab.email == email).update(user_info)
        else:
            new_user = UserTab(**user_info)
            db.session.add(new_user)
    except Exception as e:
        print(f"{e}\n{traceback.format_exc()}")
        db.session.rollback()
    else:
        db.session.commit()


def init_users():
    user_list = [
        {"username": "Jack", "email": "jack@gmail.com", "age": 25},
        {"username": "Alice", "email": "alice@163.com", "age": 22}
    ]
    for user in user_list:
        add_into_database(user)


def get_users():
    try:
        users = UserTab.query.all()
    except Exception as e:
        print(f"{e}\n{traceback.format_exc()}")
        return []
    else:
        return [user.to_dict() for user in users]
