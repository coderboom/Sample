class Test:
    def prt(self):
        print(self)
        print(self.__class__)


# t = Test()
# t.prt()  # <__main__.Test object at 0x0000021D07A485F8>
#          # <class '__main__.Test'>
class AA:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = AA(2, 3)
AA.aa = 11
a.aa = 22
print(AA.aa)  # AA.aa=11，通过类名修改类变量，可以更改其值
# a.aa=22,当a这个对象去操作aa时，会在a这个对象上新建一个aa的变量，
# 在查找的时候，按照从下往上的原则，优先查找a的aa，当找到后，就不会再去查找AA的aa。
print(a.x, a.y, a.aa)
"""
见python的自省机制
"""
