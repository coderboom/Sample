"""
什么是元类，
元类是创建类的类

python中类的实列化过程，首先会寻找Metaclass，通过metaclass去创建user类,最后回去找tpye的
"""

from collections.abc import *


class MetaClass1(type):
    def __new__(mcs, *args, **kwargs):
        return super().__new__(mcs, *args, **kwargs)


class User(metaclass=MetaClass1):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'user'


if __name__ == '__main__':
    my = User(name='boby')
    pass
