"""
create by  gaowenfeng on  2018/6/1
"""
from flask import  request, render_template, flash
from app.libs.helper import is_isbn_or_key
from app.forms.book import SearchForm
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel

from . import web


__author__ = "gaowenfeng"


@web.route("/book/search/")
def search():
    """
    搜索书籍路由
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            page = form.page.data
            yushu_book.search_by_key(q, page)

        books.fill(yushu_book, q)
    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")

    return render_template("search_result.html", books=books)


@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template("book_detail.html", book=book, wishes=[], gifts=[])
