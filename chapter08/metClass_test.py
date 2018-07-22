"""
什么是元类，
元类是创建类的类

python中类的实列化过程，首先会寻找Metaclass，通过metaclass去创建user类
"""


class MetaClass1(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass1):
    # def __init__(self):
    #     print('_________')
    pass


if __name__ == '__main__':
    my = User()
    pass
