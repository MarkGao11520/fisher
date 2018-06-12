from app.models.user import User
from . import web

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('web.login'))

    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email).first()
        if user and user.check_password(user.password):
            login_user(user, remember=True)
        else:
            flash("账号不存在或者密码错误")
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
