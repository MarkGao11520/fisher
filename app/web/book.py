"""
create by  gaowenfeng on  2018/6/1
"""
from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookCollection
import json

from . import web


__author__ = "gaowenfeng"


@web.route("/book/search/")
def search():
    """
    搜索书籍路由
    """
    form = SearchForm(request.args)
    if not form.validate():
        return jsonify(form.errors)

    q = form.q.data.strip()
    isbn_or_key = is_isbn_or_key(q)

    books = BookCollection()
    yushu_book = YuShuBook()

    if isbn_or_key == 'isbn':
        yushu_book.search_by_isbn(q)
    else:
        page = form.page.data
        yushu_book.search_by_key(q, page)

    books.fill(yushu_book, q)
    return json.dumps(books, default=lambda o: o.__dict__)
