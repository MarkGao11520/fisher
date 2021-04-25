"""
create by  gaowenfeng on  2018/5/31
"""
__author__ = "gaowenfeng"

DEBUG = True
HOST = "0.0.0.0"
PORT = 8090

SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:root@localhost:3306/fisher"
# SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = ""

# email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1152057576@qq.com'
# QQ邮箱->设置->账户->[POP3...]->生成授权码->发送短信->获取授权码
MAIL_PASSWORD = ''


