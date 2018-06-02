"""
create by  gaowenfeng on  2018/6/1
"""
from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm

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

    print(form.validate())
    q = form.q.data.strip()
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        page = form.page.data
        result = YuShuBook.search_by_key(q, page)

    return jsonify(result)
