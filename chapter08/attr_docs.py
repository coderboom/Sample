"""
属性描述符
实现了set和get： 叫数据描述符
只实现了get： 叫非数据描述符

"""
import numbers


class IntField(object):
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if isinstance(value, numbers.Integral):
            self.value = value

    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()


"""
                    属性查找过程
如果user是某个类的实例，那么user.age（以及等价的getattr（user,'age'））
首先调用__getattribute__.如果类定义的了__getattr__方法，
那么在__getattribute__抛出AttributeError的时候就会调用__getattr__
而对于描述符(__get__)的调用，则是发生在__getattribute__内部的。
------------也就是说，__get__调用早于__getattr__


(1)如果‘age’是出现在User或基类的__dict__中，且age是data descriptor ，那么调用其__get__，否则(2)
(2)如果‘age’是出现在对象(obj)的__dict__中，那么直接返回obj.__dict__['age'],否则(3)
(3)如果‘age’是出现在User或基类的__dict__中
    1> 如果‘age’是non——data descriptor ，那么调用其__get__方法，否则2>
    2>返回__dict__['age']
(4)如果User有__getattr__方法，就调用__getattr__方法，否则(5)
(5)抛出AttributeError
"""

if __name__ == '__main__':
    user = User()
    user.age = 20
    print(getattr(user, 'age'))
    print(user.age)
