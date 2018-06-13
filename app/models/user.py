from werkzeug.security import generate_password_hash,check_password_hash

__author__ = 'gaowenfeng'

from sqlalchemy import Column
from sqlalchemy import Integer, Float
from sqlalchemy import String, Boolean
from flask_login import UserMixin
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.models.wish import Wish
from app.models.gift import Gift

from app.models.base import Base
from app import login_manager


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
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        """
        判断可以将书籍加入心愿清单
        1.如果isbn编号不符合规则，不允许添加
        2.如果isbn编号对应的书籍不存在，不允许添加
        3.同一个用户，不能同时赠送同一本书籍
        4.一个用户对于一本书不能既是赠书者，又是索要者
        5.3和4合并成一条，就是一本书必须即不在心愿清单又不在赠书列表里才可以添加
        :param isbn:
        :return:
        """
        if not is_isbn_or_key(isbn):
            return False

        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        return not wishing and not gifting

    @property
    def has_in_gifts(self):
        return Gift.query.filter_by(uid=self.id).first() is not None

    @property
    def has_in_wishs(self):
        return Wish.query.filter_by(uid=self.id).first() is not None

    @login_manager.user_loader
    def get_user(uid):
        return User.query.get(int(uid))
