"""
create by  gaowenfeng on  2018/6/1
"""
__author__ = "gaowenfeng"


def is_isbn_or_key(word):
    """
        判断word是isbn号还是查询关键字key
        isbn isbn13 由13个0-9在数字组成
        isbn10 由10表0-9表数字组组成，中间可能包含' - '
    :param word:
    :return: key or isbn
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
