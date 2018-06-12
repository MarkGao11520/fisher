"""
create by gaowenfeng on 
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SmallInteger, Column
from sqlalchemy.orm import Query

__author__ = "gaowenfeng"


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
