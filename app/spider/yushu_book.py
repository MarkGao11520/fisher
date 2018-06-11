"""
create by  gaowenfeng on  2018/6/1
"""
from app.libs.httper import HTTP
from flask import current_app

__author__ = "gaowenfeng"


class YuShuBook:

    search_by_isbn_url = "http://t.yushu.im/v2/book/isbn/{}"

    search_by_key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.search_by_isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_key(self, q, page=1):
        url = self.search_by_key_url.format(q, current_app.config["PRE_PAGE"],
                                           self.__calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.books = [data]
            self.total = 1

    def __fill_collection(self, data):
        self.books = data['books']
        self.total = data['total']

    def __calculate_start(self, page):
        return (page-1) * current_app.config["PRE_PAGE"]
