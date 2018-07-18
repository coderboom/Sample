"""
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
    @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
    此时，@property本身又创建了另一个装饰器@fee.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
"""


class Fees(object):

    def __init__(self, name):
        """Constructor"""
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("输入的名字错误")

    def __getattr__(self, item):  # 当查找的元素不存在这个类中时会调用到
        return 'not find attr'


if __name__ == '__main__':
    f = Fees('abcd')
    # print(f.name)
    # f.name = "13456"
    # print(f.name)
    print(f.age)  # 返回not find attr，会调用__getattr__这个魔法函数
