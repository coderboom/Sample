"""
python 的自省机制
自省：是通过一定的机制查询到对象的内部结构

"""
from chapter04.class_method import Date


class User:
    def __init__(self, birthday):
        self.birthday = birthday

    def get_age(self):
        return 2018 - self.birthday.year


if __name__ == '__main__':
    user_ = User(Date.from_string('2011-2-3'))
    print(user_.get_age())
    print(user_)
