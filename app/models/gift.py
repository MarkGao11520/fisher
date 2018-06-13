"""
create by gaowenfeng on 
"""

from app.models.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

__author__ = "gaowenfeng"


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)