from flask import Flask
from app.models.base import db
from flask_login import LoginManager

__author__ = "gaowenfeng"

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.settings")
    # 注册蓝图
    register_blueprint(app)

    # 注册SQLAlchemy
    db.init_app(app)

    # 创建所有表
    with app.app_context():
        db.create_all()

    # 注册LoginManager
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
