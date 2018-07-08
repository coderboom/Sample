class Cat(object):
    def say(self):
        print('i am a cat!')


class Dog(object):
    def say(self):
        print('i am a dog!')


class Duck(object):
    def say(self):
        print('i am a duck!')


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()
"""
i am a cat!
i am a dog!
i am a duck!
"""


class Company(object):
    def __init__(self, emloyee_list):
        self.emloyee = emloyee_list

    def __str__(self):  # 对字符串需要格式化的时候调用
        return ','.join(self.emloyee)

    def __repr__(self):  # 开发模式下，和__str__ 一样，格式化字符串
        return ','.join(self.emloyee)

    def __getitem__(self, item):  # 定义此方法后，实列就变成一个可以被迭代的对象
        return self.emloyee[item]

    def __len__(self):
        return self.emloyee.__len__()


company = Company(['tom', 'bob', 'jane'])

a = ['bay1', 'baby2']
b = ['baby2', 'baby']
c = ['baby4', 'baby5']
d = set()
d.add('baby6')
d.add('baby7')
d.add('baby6')

a.extend(Company(c))
print(a)
