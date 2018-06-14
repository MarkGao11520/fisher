"""
create by gaowenfeng on 
"""
from threading import Thread

from app import mail
from flask_mail import Message
from flask import current_app, render_template

__author__ = "gaowenfeng"


def send_mail_async(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except:
            print('邮件发送失败')


def send_mail(to, subject, template, **kwargs):
    msg = Message(
        '[鱼书]'+' '+subject,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_mail_async, args=[app,msg])
    thr.start()
