# 需求
import numbers


class IntField(object):
    # 属性描述符

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need!')
        if value < 0:
            raise ValueError('positive value need!')
        self.value = value

    def __get__(self, instance, owner):
        return self.value


class CharField(object):
    pass


class User(object):
    name = CharField()
