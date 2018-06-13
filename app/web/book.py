"""
create by  gaowenfeng on  2018/6/1
"""
from flask import  request, render_template, flash
from flask_login import current_user

from app.forms.trade import TradeInfo
from app.libs.helper import is_isbn_or_key
from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.wish import Wish
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

    # 取出每本书的详情
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # 三种情况的判断
    has_in_gifts = current_user.is_authenticated and current_user.has_in_gifts
    has_in_wishs = current_user.is_authenticated and current_user.has_in_wishs

    # 赠书人列表和索要人列表
    trade_gifts = Gift.query.filter_by(isbn=isbn).all()
    trade_wishs = Wish.query.filter_by(isbn=isbn).all()

    trade_wishs_model = TradeInfo(trade_wishs)
    trade_gifts_model = TradeInfo(trade_gifts)
    return render_template("book_detail.html", book=book,
                           wishes=trade_wishs_model, gifts=trade_gifts_model,
                           has_in_wishs=has_in_wishs, has_in_gifts=has_in_gifts)
