"""
create by  gaowenfeng on  2018/6/1
"""
from httper import HTTP

__author__ = "gaowenfeng"


class YuShuBook:

    search_by_isbn_url = "http://t.yushu.im/v2/book/search/isbn/{}"

    search_by_key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.search_by_isbn_url.format(isbn)
        return HTTP.get(url)

    @classmethod
    def search_by_key(cls, q, count=15, start=0):
        url = cls.search_by_key_url.format(q, count, start)
        return HTTP.get(url)
