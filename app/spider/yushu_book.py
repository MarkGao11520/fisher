"""
create by  gaowenfeng on  2018/6/1
"""
from app.libs.httper import HTTP
from flask import current_app

__author__ = "gaowenfeng"


class YuShuBook:

    search_by_isbn_url = "http://t.yushu.im/v2/book/search/isbn/{}"

    search_by_key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.search_by_isbn_url.format(isbn)
        return HTTP.get(url)

    @classmethod
    def search_by_key(cls, q, page=1):
        url = cls.search_by_key_url.format(q, current_app.config["PRE_PAGE"],
                                           cls.calculate_start(page))
        return HTTP.get(url)

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config["PRE_PAGE"]
