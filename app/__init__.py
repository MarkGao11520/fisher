from flask import Flask

__author__ = "gaowenfeng"


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.settings")
    register_blueprint(app)

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
