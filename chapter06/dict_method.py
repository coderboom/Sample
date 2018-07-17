# a = dict
a = {'boby1': {"company": 'imooc'}, 'boby2': {'company': 'imooc2'}}

new_a1 = a.copy()  # 浅拷贝 只拷贝第一层，2层及以上 都是拷贝元素的地址
new_a1['boby1']['company'] = 'aaaaa'
# 在浅拷贝中，由于value是一个dict，new_a1['boby1']指向{"company": 'imooc'}，所以是可以更改‘company’的value的

import copy  # 深拷贝

"""
深拷贝 
"""
new_a2 = copy.deepcopy(a)
new_a2['boby1']['company'] = 'bbbbbb'
"""
formkeys :用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
"""
b = ['boby1', 'boby2']
new3 = dict.fromkeys(b, {"company": 'imooc'})
print(new3)

"""
get(): 用于取值，若key不存在，返回空，key存在，换回对应的value
"""
value1 = a.get('baby')  # return None
print(value1)
value2 = a.get('boby1')  # return {'company': 'aaaaa'}
print(value2)

"""
items(): 遍历
"""
for key, value in a.items():
    print(key, "-->", value)
"""
setdefault(): 当查找的key，value不存在时，便会将这个key：value插入到原dict中
"""
default = a.setdefault('baby', 'ccccccc')
print(default)

pass
