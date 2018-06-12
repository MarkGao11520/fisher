"""
create by gaowenfeng on 
"""

from app.models.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationships

__author__ = "gaowenfeng"


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=True)
    launched = Column(Boolean, default=False)
