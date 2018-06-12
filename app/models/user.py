from werkzeug.security import generate_password_hash,check_password_hash

__author__ = 'gaowenfeng'

from sqlalchemy import Column
from sqlalchemy import Integer, Float
from sqlalchemy import String, Boolean
from flask_login import UserMixin

from app.models.base import Base


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128))
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)
