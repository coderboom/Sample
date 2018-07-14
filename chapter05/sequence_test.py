"""
自定义序列化
"""
from collections import abc

"""
+ :
"""
a = [1, 2, 3]
b = a + [4, 5, 6]
print(b)
"""
+= :就地加
"""
a += [7, 8, 9]
print(a)

a += (11, 12, 13)
print(a)

a += {14: 15, 16: 17}
print(a)

"""
.extend(A)

extend()，无返回值，直接作用在对象上
"""
a.extend(range(20, 25))
print(a)
