# -*- coding: utf-8 -*-
import time
import traceback
from models import db
from sqlalchemy.dialects.mysql import INTEGER, BIGINT, VARCHAR, TEXT, TINYINT


class UserTab(db.Model):
    id = db.Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(BIGINT(unsigned=True), unique=True, nullable=False)
    name = db.Column(VARCHAR(length=32), nullable=False)
    email = db.Column(VARCHAR(length=64), unique=True, nullable=False)
    credential = db.Column(TEXT, nullable=False)
    create_time = db.Column(BIGINT(unsigned=True), nullable=False)
    update_time = db.Column(BIGINT(unsigned=True), nullable=False)
    expire_time = db.Column(BIGINT(unsigned=True), nullable=False)
    is_valid = db.Column(TINYINT(display_width=1, unsigned=True), nullable=False, default=1)

    def __repr__(self):
        return f"<User(id={self.id}, user_id={self.user_id}, name={self.name}, email={self.email})>"

    def to_dict(self):
        model_dict = dict()
        for c in self.__table__.columns:
            value = getattr(self, c.name, None)
            if value is None:
                value = ""
            model_dict[c.name] = value
        return model_dict


def add(user_info):
    user_info.update({"create_time": round(time.time() * 1000)})
    user_info.update({"update_time": round(time.time() * 1000)})
    user_info.update({"expire_time": round((time.time() + 24 * 60 * 60) * 1000)})
    try:
        db.session.add(UserTab(**user_info))
    except Exception as e:
        print(f"{e}\n{traceback.format_exc()}")
        db.session.rollback()
    else:
        db.session.commit()


def update(user_info):
    user_info.update({"update_time": round(time.time() * 1000)})
    user_info.update({"expire_time": round((time.time() + 24 * 60 * 60) * 1000)})
    try:
        UserTab.query.filter(UserTab.user_id == user_info["user_id"]).update(user_info)
    except Exception as e:
        print(f"{e}\n{traceback.format_exc()}")
        db.session.rollback()
    else:
        db.session.commit()
        

def get_user_by_user_id(user_id):
    try:
        user = UserTab.query.filter(UserTab.user_id == user_id).one()
    except Exception as e:
        print(f"{e}\n{traceback.format_exc()}")
        return {}
    else:
        return user.to_dict()


def init_users():
    user_list = [
        {"user_id": 1, "name": "Pony Ma", "email": "pony.ma@gmail.com", "credential": "credential.1"},
        {"user_id": 2, "name": "Jack Ma", "email": "jack.ma@gmail.com", "credential": "credential.2"},
        {"user_id": 3, "name": "Stephen Chow", "email": "stephen.chow@gmail.com", "credential": "credential.3"},
        {"user_id": 4, "name": "Elon Musk", "email": "elon.musk@gmail.com", "credential": "credential.4"},
        {"user_id": 5, "name": "Allen Walker", "email": "allen.walker@gmail.com", "credential": "credential.5"},
        {"user_id": 6, "name": "Michael Jackson", "email": "michael.jackson@gmail.com", "credential": "credential.6"},
        {"user_id": 7, "name": "Albert Einstein", "email": "albert.einstein@gmail.com", "credential": "credential.7"},
        {"user_id": 8, "name": "Steve Jobs", "email": "steve.jobs@gmail.com", "credential": "credential.8"},
        {"user_id": 9, "name": "Nelson Mandela", "email": "nelson.mandela@gmail.com", "credential": "credential.9"},
        {"user_id": 10, "name": "Marie Curie", "email": "marie.curie@gmail.com", "credential": "credential.10"},
        {"user_id": 11, "name": "Isaac Newton", "email": "isaac.newton@gmail.com", "credential": "credential.11"},
        {"user_id": 12, "name": "Nikola Tesla", "email": "nikola.tesla@gmail.com", "credential": "credential.12"},
    ]
    for user in user_list:
        add(user)


def get_users(page=1, size=0):
    try:
        if not size:
            users = UserTab.query.order_by(UserTab.id.desc()).all()
        else:
            users = UserTab.query.order_by(UserTab.id.desc()).paginate(page=page, per_page=size).items
    except Exception as e:
        print(f"{e}\n{traceback.format_exc()}")
        return []
    else:
        return [user.to_dict() for user in users]
