"""
create by gaowenfeng on 
"""

from app.models.base import Base, db
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, func, desc
from sqlalchemy.orm import relationship

from app.spider.yushu_book import YuShuBook

__author__ = "gaowenfeng"


class Wish(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=True)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_user_wishes(cls, uid):
        from app.models.gift import Gift

        wishes = Wish.query \
            .filter_by(uid=uid, launched=False) \
            .order_by(desc(Wish.create_time)) \
            .all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        from app.models.gift import Gift

        # 根据传入的一组isbn编号，到Wish表中计算出某个礼物的Wish心愿数量
        # select count(id),isbn from wish
        # where launched = false and isbn in ('','') and status =1 group by isbn

        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        # 不要将tuple返回到外部，应该返回有意义的字典或者对象
        count_list = [{'count': w[0], 'isbn':w[1]} for w in count_list]
        return count_list

    @classmethod
    def get_user_wishes_by_orm(cls, uid):
        from app.models.gift import Gift
        wishes = db.session\
            .query(Wish, func.count(Gift.id))\
            .outerjoin(Gift, Gift.isbn == Wish.isbn)\
            .filter(
                Gift.launched == False,
                Wish.launched == False,
                Gift.status == 1,
                Wish.status == 1,
                Wish.uid == uid)\
            .group_by(Wish.id, Wish.isbn)\
            .order_by(desc(Wish.create_time))\
            .all()
        wishes = [{'wish': wish[0], 'count':wish[1]} for wish in wishes]
        return wishes
