"""
create by gaowenfeng on 
"""

__author__ = "gaowenfeng"


class A:
    def __call__(self):
        return object()


class B:
    def __call__(self):
        return object()


def func():
    return object()


def main(callable):
    # 我想在main中传入一个参数，得到一个对象object
    callable()
    pass


main(A())
main(B())
main(func)
