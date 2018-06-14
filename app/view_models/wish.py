"""
create by gaowenfeng on 
"""
from app.view_models.book import BookViewModel

__author__ = "gaowenfeng"


class Wishes:

    def __init__(self, wishes_of_mine):
        self.wishes = []
        self.__wishes_of_mine = wishes_of_mine

        self.wishes = self.__parse()

    def __parse(self):
        temp_list = [self.__parse_single(wish) for wish in self.__wishes_of_mine]
        return temp_list

    def __parse_single(self, wish):
        r = {
            'wishes_count': wish['count'],
            'book': BookViewModel(wish['wish'].book),
            'id': wish['wish'].id
        }
        return r
