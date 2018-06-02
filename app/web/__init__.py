from flask import Blueprint

__author__ = "gaowenfeng"


web = Blueprint('web', __name__)

from app.web import book
from app.web import user

