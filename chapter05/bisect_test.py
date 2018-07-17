import bisect

# 用来处理已排序的序列，用来维持已排序的序列——升序
# 查找算法：二分法
a = []
bisect.insort(a, 2)
bisect.insort(a, 5)
bisect.insort(a, 6)
bisect.insort(a, 1)
bisect.insort(a, 4)
bisect.insort(a, 9)
bisect.insort(a, 0)
bisect.insort(a, 0)
bisect.insort(a, 6)
bisect.insort(a, 6)

print(a)  # [0, 0, 1, 2, 4, 5, 6, 6, 6, 9]
print(bisect.bisect(a, 6))  # 9    bisect(序列名，要查找的元素)，默认返回最后一个相同元素的索引的下一位
print(bisect.bisect_left(a, 6))  # 6  返回相同元素中的第一个的索引
