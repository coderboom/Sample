"""
列表生成式（列表推导式）  :[]
1、[表达式 for 变量 in 列表]
2、[表达式 for 变量 in 列表 if 条件]
列表生成式性能高于列表操作
"""


# 简单
# o = []
# for i in range(0, 21):
#     if i % 2 == 1:
#         o.append(i)
#
# o = [i for i in range(0, 21) if i % 2 == 1]


# 逻辑复杂情况

def handle_item(item):
    return item ** 2


o = [handle_item(i) for i in range(0, 21) if i % 2 == 1]
print(o)
"-------------------------------------------------------------"
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x ** 2 for x in li])
print([x ** 2 for x in li if x > 5])
print(dict([(x, x * 10) for x in li]))
print([(x, y)
       for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8])

vec = [2, 4, 6]
vec2 = [4, 3, -9]
sq = [vec[i] + vec2[i] for i in range(len(vec))]
print(sq)
print([x * y for x in [1, 2, 3] for y in [1, 2, 3]])
testList = [1, 2, 3, 4]


def mul2(x):
    return x * 2


print([mul2(i) for i in testList])

"""
生成器表达式  :()
"""
o_gen = (handle_item(i) for i in range(0, 21) if i % 2 == 1)
print(type(o_gen))
print(o_gen)
# for i in o:
#     print(i)

o_list = list(o_gen)  # 将生成器转成list
print(o_list)

"""
字典推导式 {}
"""

my_dict = {'boby1': 22, 'boby2': 11, 'backd': 33}
reversed_dict = {value: key for key, value in my_dict.items()}
print(my_dict)
print(reversed_dict)

"""
集合推导式  set
"""
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)
