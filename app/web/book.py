"""
create by  gaowenfeng on  2018/6/1
"""
from flask import jsonify,Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook


__author__ = "gaowenfeng"


# 实例化蓝图
web = Blueprint('web', __name__)


@web.route("/book/search/<q>/<page>")
def search(q, page):
    """
    搜索书籍路由
    :param q: 关键字 OR isbn
    :param page: 页码
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_key(q)

    return jsonify(result)
