"""
create by gaowenfeng on 
"""

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

__author__ = "gaowenfeng"

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=True)
    author = Column(String(30), default="未名")
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    isbn = Column(String(15), nullable=True, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))


