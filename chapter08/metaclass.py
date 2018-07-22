# def createClass(clasName):
#     if clasName == 'User':
#         class User(object):
#             def __init__(self):
#                 print('I am user class')
#
#         return User
#     if clasName == 'Person':
#         class Person(object):
#             def __init__(self):
#                 print('I am person class')
#
#         return Person
#     else:
#         return 'None'


def ruanjian(self):
    print('我学的是软件工程专业')


def answer(self):
    print('I am student')


class BaseClass(object):
    def answer(self):
        print('I am BaseClass')


if __name__ == '__main__':
    # My = createClass('Person')
    # my = My()

    """
    type 动态创建类
    type(类名,继承的基类（tuple类型）,{属性和方法名（dict类型）})
    """
    Student = type('Student', (BaseClass,), {'name': 'chenhao',
                                             'ruanjian': ruanjian, 'answer': answer})
    s = Student()
    print(s.name)
    s.ruanjian()
    s.answer()
    pass
