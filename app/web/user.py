"""
create by gaowenfeng on 
"""

from . import web

__author__ = "gaowenfeng"


@web.route("/user/login")
def login():
    return "success"
