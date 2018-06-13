from . import web


__author__ = '七月'


@web.route('/')
def index():
    return "index"


@web.route('/personal')
def personal_center():
    pass
