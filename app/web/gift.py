from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user
from flask import flash, current_app, render_template, redirect, url_for
from app.models.base import db
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return "my gifts"


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id

            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']

            db.session.add(gift)
            db.session.add(current_user)
    else:
        flash("这本书以添加进您的赠送清单或已经存在于您的心愿清单，请不要重复添加")
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



